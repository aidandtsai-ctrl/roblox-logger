import os
import requests
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# --- Your existing bot code ---
webhook_url = os.environ.get('WEBHOOK_URL')

def send_to_discord(message):
    if webhook_url:
        data = {"content": message}
        try:
            requests.post(webhook_url, json=data)
        except Exception as e:
            print(f"Error sending to Discord: {e}")

# --- A simple web server to satisfy Render ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

if __name__ == "__main__":
    print("Starting web server to keep bot alive...")
    threading.Thread(target=run_server, daemon=True).start()
    
    print("Bot is starting...")
    send_to_discord("The bot is now online!")
    
    while True:
        time.sleep(60)