import cv2
import mediapipe as mp
import math
import numpy as np
from pycaw.pycaw import AudioUtilities


# ============================================================
# MEDIAPIPE SETUP
# ============================================================

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


# ============================================================
# WINDOWS VOLUME SETUP
# ============================================================

devices = AudioUtilities.GetSpeakers()

# Newer Pycaw API
volume = devices.EndpointVolume

minVol, maxVol, _ = volume.GetVolumeRange()


# ============================================================
# WEBCAM SETUP
# ============================================================
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Could not open webcam.")
    exit()


# ============================================================
# INITIAL VALUES
# ============================================================

volBar = 400
volPer = 0

# Used for smoother volume movement
smoothVolPer = 0


# ============================================================
# MAIN LOOP
# ============================================================

while True:

    success, frame = cap.read()

    if not success:
        print("Could not read from webcam.")
        break

    # Mirror the webcam
    frame = cv2.flip(frame, 1)

    # Convert BGR -> RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)


    # --------------------------------------------------------
    # Reset finger positions every frame
    # --------------------------------------------------------

    thumb = None
    index = None


    # --------------------------------------------------------
    # HAND DETECTED
    # --------------------------------------------------------

    if results.multi_hand_landmarks:

        # Only use the first detected hand
        hand_landmarks = results.multi_hand_landmarks[0]

        h, w, c = frame.shape


        # ----------------------------------------------------
        # Get thumb and index finger positions
        # ----------------------------------------------------

        for id, landmark in enumerate(hand_landmarks.landmark):

            cx = int(landmark.x * w)
            cy = int(landmark.y * h)

            # Thumb tip
            if id == 4:
                thumb = (cx, cy)

                cv2.circle(
                    frame,
                    thumb,
                    12,
                    (255, 0, 255),
                    -1
                )

            # Index finger tip
            if id == 8:
                index = (cx, cy)

                cv2.circle(
                    frame,
                    index,
                    12,
                    (255, 0, 255),
                    -1
                )


        # ----------------------------------------------------
        # Calculate distance between thumb and index
        # ----------------------------------------------------

        if thumb is not None and index is not None:

            # Draw line between thumb and index
            cv2.line(
                frame,
                thumb,
                index,
                (0, 255, 0),
                3
            )


            # Calculate distance
            length = math.hypot(
                index[0] - thumb[0],
                index[1] - thumb[1]
            )


            # ------------------------------------------------
            # Map finger distance to Windows volume
            # ------------------------------------------------

            vol = np.interp(
                length,
                [30, 200],
                [minVol, maxVol]
            )

            volume.SetMasterVolumeLevel(vol, None)


            # ------------------------------------------------
            # Calculate volume bar
            # ------------------------------------------------

            volBar = np.interp(
                length,
                [30, 200],
                [400, 150]
            )


            # ------------------------------------------------
            # Calculate percentage
            # ------------------------------------------------

            volPer = np.interp(
                length,
                [30, 200],
                [0, 100]
            )


            # Smooth percentage
            smoothVolPer = 0.8 * smoothVolPer + 0.2 * volPer


        # Draw MediaPipe hand landmarks
        mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )


    # ========================================================
    # VOLUME BAR
    # ========================================================

    # Outer volume bar
    cv2.rectangle(
        frame,
        (50, 150),
        (85, 400),
        (0, 255, 0),
        3
    )


    # Filled volume bar
    cv2.rectangle(
        frame,
        (50, int(volBar)),
        (85, 400),
        (0, 255, 0),
        cv2.FILLED
    )


    # ========================================================
    # VOLUME PERCENTAGE
    # ========================================================

    cv2.putText(
        frame,
        f"{int(smoothVolPer)}%",
        (40, 440),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        3
    )


    # ========================================================
    # TITLE
    # ========================================================

    cv2.putText(
        frame,
        "Gesture Volume Control",
        (100, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )


    # ========================================================
    # EXIT INSTRUCTION
    # ========================================================

    cv2.putText(
        frame,
        "Press Q to quit",
        (100, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


    # ========================================================
    # SHOW CAMERA
    # ========================================================

    cv2.imshow(
        "Gesture Volume Control",
        frame
    )


    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ============================================================
# CLEANUP
# ============================================================

cap.release()
cv2.destroyAllWindows()
hands.close()