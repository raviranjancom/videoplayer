# Mr Player 🎬

A lightweight, cross-platform media player built with Python and PyQt5. Designed with a focus on clean state management and modular UI architecture, Mr Player interfaces directly with native OS multimedia frameworks (GStreamer on Linux, Media Foundation on Windows) to deliver reliable video rendering.
✨ Current Features

    Cross-Platform Compatibility: Runs seamlessly on both Windows 11 and Linux environments.

    Native Hardware Decoding: Utilizes the underlying OS multimedia pipelines for efficient video playback without heavy overhead.

    Dynamic Media Loading: Supports injecting absolute file paths at runtime to switch video streams dynamically.

    Unified State Management: Play/Pause controls are strictly synchronized with the underlying engine's state machine, preventing command collisions.

⚙️ Prerequisites & System Requirements

Before running the application, ensure you have Python 3.x installed along with the required Python libraries.
Bash

pip install PyQt5

OS-Specific Dependencies:

    Windows 11: No additional installation required. It uses native Windows Media Foundation.

    Linux (Ubuntu/Debian): You must install the GStreamer backend and audio/video codecs to prevent segmentation faults during decoding.
    Bash

    sudo apt-get update
    sudo apt-get install gstreamer1.0-libav gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-pulseaudio gstreamer1.0-alsa gstreamer1.0-plugins-good

🚀 How to Run

    Clone or download this repository to your local machine.

    Open your terminal or command prompt and navigate to the project directory.

    Execute the main Python script:

Bash

python3 main.py

(Note for Linux Wayland users: If the video stutters or freezes on the first frame, force the X11 rendering backend by running: QT_QPA_PLATFORM=xcb python3 main.py)
🛠️ Usage

    Launch the application.

    Paste the absolute path of your .mp4 video file into the input field at the top (e.g., C:\Videos\my_video.mp4 for Windows or /home/user/Videos/my_video.mp4 for Linux).

    Click the Play button next to the input field to load the media into the engine.

    Use the > / || toggle button at the bottom to control playback state.

ScreenShot
![Uploading image.png…]()


Author: Ravi Ranjan
