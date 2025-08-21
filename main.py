import os
from sound_detection import record_audio, detect_specific_sound
from camera_capture import capture_image
from telegram_bot import send_notification

def main():
    """
    Main function to manage sound detection and notification process.
    """
    print("Starting AI-Based Sound Detection System...")

        # Step 1: Record audio
    audio_file = record_audio(duration=5)

        # Step 2: Detect specific sound
    is_specific_sound = detect_specific_sound(audio_file)

    if is_specific_sound:
        print("Specific sound detected!")

            # Step 3: Capture image
        image_file = capture_image()

            # Step 4: Send notification via Telegram
        send_notification(image_file, message="Specific sound detected! Check the image.")
    else:
        print("No specific sound detected.")

if __name__ == "__main__":
    main()
