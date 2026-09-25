# AirVolume

> **Control your Windows system volume with a simple hand gesture.**

AirVolume is a real-time computer vision application that turns a webcam
into a touchless volume controller. Move your **thumb and index finger
closer or farther apart** to adjust the Windows master volume instantly.

Built with Python, MediaPipe, OpenCV, NumPy, and Pycaw, AirVolume
demonstrates how computer vision can be connected to native desktop
controls to create a practical, touch-free user experience.

---

## ✨ Features

- 🎥 **Real-time hand tracking** using MediaPipe
- 🤏 **Intuitive gesture control** using thumb–index finger distance
- 🔊 **Native Windows volume control** through Pycaw
- 📊 **Live volume percentage and visual volume bar**
- ⚡ **Smooth volume updates** to reduce jitter
- 🖥️ **Standalone Windows executable** — no Python installation required for end users
- 🧹 Lightweight interface with simple keyboard controls

---

## 🎬 How It Works

AirVolume follows a straightforward computer-vision pipeline:

```text
Webcam
   ↓
OpenCV frame capture
   ↓
MediaPipe hand landmark detection
   ↓
Thumb + index finger positions
   ↓
Distance calculation
   ↓
Distance mapped to volume range
   ↓
Pycaw
   ↓
Windows master volume
```

The distance between the thumb and index finger is mapped to the available Windows audio volume range:

```text
Fingers closer  →  Lower volume
Fingers farther →  Higher volume
```

A smoothing filter is also applied to the displayed percentage to make the visual feedback more stable.

---

## 🖥️ Demo

### Gesture

Hold one hand in front of your webcam and control the volume by changing the distance between your thumb and index finger.

| Gesture | Action |
|---|---|
| 🤏 Fingers close together | Decrease volume |
| 🖐️ Fingers farther apart | Increase volume |
| `Q` | Exit the application |

> **Tip:** Keep your hand clearly visible to the webcam and make gradual movements for the smoothest control.

---

## 🚀 Run the Application

### Option 1 — Download the Windows executable

For users who simply want to use AirVolume, download the latest Windows executable from the project's **GitHub Releases** page.

```text
AirVolume.exe
```

No Python setup is required when using the packaged executable.

### Option 2 — Run from source

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AirVolume.git
cd AirVolume
```

Create and activate a virtual environment:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Run the application:

```powershell
python main.py
```

Press **Q** to exit.

---

## 📦 Build the Windows Executable

AirVolume can be packaged using PyInstaller:

```powershell
pyinstaller --clean --onefile --windowed --name AirVolume --collect-all mediapipe main.py
```

The executable will be generated in:

```text
dist/AirVolume.exe
```

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.12** | Application development |
| **MediaPipe** | Hand landmark detection |
| **OpenCV** | Webcam capture and visual interface |
| **NumPy** | Gesture-to-volume mapping |
| **Pycaw** | Windows audio control |
| **PyInstaller** | Standalone Windows packaging |

---

## 📁 Project Structure

```text
AirVolume/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
└── dist/
    └── AirVolume.exe
```

The local `.venv/` directory is intentionally excluded from version control.

---

## ⚙️ Requirements

### For running from source

- Windows 10 or Windows 11
- Python 3.12
- A working webcam
- Windows audio output device

### For the packaged executable

- Windows 10 or Windows 11
- A working webcam
- Windows audio output device

---

## 🔐 Privacy

AirVolume processes webcam frames locally on the user's computer.

The application does not require an internet connection for gesture detection or volume control, and it does not upload webcam frames to a remote server.

---

## 🛠️ Troubleshooting

### Webcam does not open

Make sure:

- Your webcam is connected and available.
- Windows has granted camera access to desktop applications.
- Another application is not exclusively using the webcam.

### Gesture tracking is inaccurate

Try:

- Improving the lighting.
- Moving your hand farther from the camera.
- Keeping your entire hand within the camera frame.
- Avoiding a cluttered background.

### Volume does not change

Make sure:

- AirVolume is running on Windows.
- A valid Windows audio output device is available.
- The application has access to the Windows audio endpoint.

---

## 🔮 Future Improvements

Potential improvements include:

- [ ] Adjustable gesture sensitivity
- [ ] Customizable minimum and maximum volume thresholds
- [ ] Mute gesture
- [ ] Multi-hand gesture support
- [ ] Customizable UI
- [ ] System tray mode
- [ ] Configuration file for user preferences
- [ ] Additional gesture-controlled system actions

---

## 🎯 Project Goals

AirVolume was built to explore the practical combination of:

- Computer vision
- Real-time gesture recognition
- Human–computer interaction
- Native Windows system integration
- Desktop application packaging

The project demonstrates how camera-based hand landmarks can be translated into meaningful system-level controls.

---

## 👤 Author

**Srajal Singh**

B.Tech CSE

If you find the project interesting, feel free to explore the source code, try the application, or build your own gesture-controlled desktop experience.

---

## 📄 License

This project is available under the **MIT License**.

See [`LICENSE`](LICENSE) for details.
