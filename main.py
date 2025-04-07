import time
import requests
from playwright.sync_api import sync_playwright
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

def check_tickets():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()
        page.goto("https://shop.royalchallengers.com/ticket", timeout=60000)
        page.wait_for_timeout(5000)  
        elements = page.query_selector_all(".chakra-text.css-1nm99ps")
        for el in elements:
            text = el.inner_text()
            if "May" in text:
                message = "May Tickets Available!\nLogin to https://shop.royalchallengers.com/ticket and get yours now!"
                send_telegram_message(message)

        browser.close()

def check_loop():
    while True:
        try:
            check_tickets()
        except Exception as e:
            send_telegram_message(f"Error: {str(e)}")
        time.sleep(300)

if __name__ == '__main__':
    check_loop()