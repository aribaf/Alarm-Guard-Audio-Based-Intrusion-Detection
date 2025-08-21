# Alarm-Guard: Audio-Based Intrusion Detection with Camera & Telegram Alerts

Alarm-Guard is a **Python-based AI alarm system** designed to detect intrusion or suspicious activity using both **video and audio signals**. The system watches through a camera feed and listens for alarming noises—such as breaking glass, footsteps, or forced entries—and immediately notifies the owner via a **Telegram bot**.

---

##  Features

- **Video Detection**: Monitors real-time video to identify unauthorized presence, suspicious movement, or potential theft.  
- **Audio Detection**: Analyzes ambient sounds to detect alarms or unusual noise patterns (e.g., glass shattering, forced entry).  
- **Smart Notifications**: Sends instant alerts—including images and/or audio snippets—to the owner's Telegram account via a dedicated bot.  
- **Cross-Modal Security**: By combining visual and acoustic sensing, Alarm-Guard offers a more robust and reliable intrusion detection experience.  
- **Modular & Customizable**: Components for camera input, noise detection, and Telegram messaging are decoupled, enabling easy adjustments and expansion.  
- **Easy Setup**: Compatible with standard Python environments and widely-available libraries.

---

##  How It Works

1. **Capture**: Continuously captures frames from the camera and audio from the microphone.  
2. **Analyze**: Applies machine learning models (e.g., OpenCV, TensorFlow, or audio-processing libraries) to detect entropy in visual or acoustic input.  
3. **Alert**: On detecting an anomaly, generates a snapshot or audio clip and sends an alert via Telegram with embedded multimedia.  
4. **Respond**: The owner receives the notification and can take swift action remotely.

---
![Project Screenshot](assets/images/)

##  Why Use Alarm-Guard?

Traditional alarms often rely on motion sensors or single-channel detection, increasing false positives. Alarm-Guard's **dual detection mode**—visual plus audio—improves accuracy and flexibility. Whether it's suspicious motion or a loud disruptive sound (like a window breaking), you'll be alerted in real time, making this system ideal for smart home protection or small business surveillance.

---

##  Project Structure & Setup

- `camera_detection/`: Video capture and analysis modules  
- `audio_detection/`: Audio processing and anomaly detection code  
- `telegram_bot/`: Bot scripts for sending alerts (setup instructions included)  
- `requirements.txt`: Dependencies list  
- `README.md`: Detailed setup, installation steps, and usage examples

