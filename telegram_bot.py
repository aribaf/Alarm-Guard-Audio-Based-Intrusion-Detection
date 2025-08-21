import telebot
from telebot import apihelper
import requests

API_TOKEN = "7595837454:AAGNfI5AQ6BS6gNApFP_wjGzqTs3qYwz3GU"
CHAT_ID = 6311286131  # The chat ID from the JSON response

# Proxy configuration (if using proxy, ensure it's accurate)
proxy = {
    'http': 'socks5h://whhegduk:sq93b0mv8uk5@198.23.239.134:6540',
    'https': 'socks5h://whhegduk:sq93b0mv8uk5@198.23.239.134:6540'
}
apihelper.proxy = proxy

bot = telebot.TeleBot(API_TOKEN)

def send_notification(image_path, message="Specific sound detected!"):
    try:
        # Send a text message
        bot.send_message(CHAT_ID, message)
        print("Text message sent successfully.")

        # Send an image or any file
        with open(image_path, 'rb') as photo:
            bot.send_photo(CHAT_ID, photo)
        print("File sent successfully.")
        
    except requests.exceptions.ConnectTimeout:
        print("Connection to Telegram API timed out. Please check your network or proxy settings.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print(f"Image file not found: {image_path}")

if __name__ == "__main__":
    # Replace 'image.jpg' with the actual image path
    send_notification("image.jpg")  # Add the file path of the image you want to send
