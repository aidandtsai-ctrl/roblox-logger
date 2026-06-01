import os
import requests
import time

# This reads the WEBHOOK_URL you set in your Render environment variables
webhook_url = os.environ.get('WEBHOOK_URL')

def send_to_discord(message):
    if webhook_url:
        data = {"content": message}
        try:
            requests.post(webhook_url, json=data)
        except Exception as e:
            print(f"Error sending to Discord: {e}")
    else:
        print("WEBHOOK_URL is not set!")

if __name__ == "__main__":
    print("Bot is starting...")
    send_to_discord("The bot is now online and connected!")
    
    # This loop prevents the script from finishing immediately, 
    # which stops the "Application exited early" error.
    while True:
        # The script will wait here for 60 seconds before repeating
        time.sleep(60)