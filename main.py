import time
import requests
from playwright.sync_api import sync_playwright

# RCB tickets booking page URL
rcb_tickets_page_url = "https://shop.royalchallengers.com/ticket"

BOT_TOKEN = "7935296753:AAGQjFN96Dte9altLNcRm2Er1DeLxjWDJpM"
CHAT_ID = "960883451"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

def check_tickets():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = browser.new_page()
        page.goto("https://shop.royalchallengers.com/ticket", timeout=60000)
        page.wait_for_timeout(5000)  # Wait 5 seconds for JS to load

        elements = page.query_selector_all(".chakra-text.css-1nm99ps")
        print('here')
        for el in elements:
            text = el.inner_text()
            if "Apr" in text:
                message = "April Tickets Available!\n"
                send_telegram_message(message)

        browser.close()

def check_loop():
    while True:
        try:
            check_tickets()
        except Exception as e:
            send_telegram_message(f"Error: {str(e)}")
        time.sleep(300)  # Check every 5 minutes

if __name__ == '__main__':
    check_loop()