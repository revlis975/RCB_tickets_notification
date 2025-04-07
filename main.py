# Standard library imports
import time
from datetime import datetime
from urllib import request

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

if __name__ == '__main__':
    check_tickets()

# while not tickets_available:
#     tickets_page = getPage(rcb_tickets_page_url)
#     tickets_bsobj = BeautifulSoup(tickets_page, features="html.parser")
#     # available_tickets_dates = get_dates_of_available_tickets(tickets_bsobj)
#     available_tickets_dates = []
#     options = Options()
#     options.add_argument('--headless=new')
#     options.add_argument('--disable-gpu')  # Optional, good for Windows
#     options.add_argument('--disable-dev-shm-usage')

#     driver = webdriver.Chrome(options=options)
#     driver.get("https://shop.royalchallengers.com/ticket")  

#     # Wait for the page to load JavaScript content
#     time.sleep(3)  # Better to use WebDriverWait for production

#     # Find the div and extract text
#     WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "chakra-text"))
#     )

#     # Find all matching elements
#     elements = driver.find_elements(By.CSS_SELECTOR, ".chakra-text.css-1nm99ps")

#     print("Found", len(elements), "elements.")
#     for elem in elements:
#         available_tickets_dates.append(elem.text)
#     # print(tickets_bsobj)

#     for available_ticket_date in available_tickets_dates:
#         # date_obj = datetime.strptime(available_ticket_date, "%A, %b %d, %Y %I:%M %p")
#         # formatted_date = date_obj.strftime("%Y-%m-%d")
#         if "Apr" in available_ticket_date:
#             print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Tickets available. Sending message...")
#             tickets_available = True
#             # msg = EmailMessage()
#             # with open(r"C://Users//HP\Downloads//RCB-Tickets-Notification-Script-main//RCB-Tickets-Notification-Script-main//rcb-tickets.txt") as fp:
#             #     msg.set_content(fp.read())
#             # msg['Subject'] = 'Test'
#             # msg['From'] = "aryanjigupta@gmail.com"
#             # msg['To'] = "aryanjigupta@gmail.com"

#             # # Send the message via our own SMTP server.
#             # s = smtplib.SMTP('localhost')
#             # s.send_message(msg)

#             email_subject = "Test"
#             email_body = "The match tickets for May are available. Login to https://shop.royalchallengers.com/ticket to book the tickets immediately."
#             send_email_alert(
#                 subject=email_subject,
#                 body=email_body,
#                 to_email='aryanjigupta@gmail.com',
#                 from_email='aryanjigupta@gmail.com',
#                 from_password="cdgp uboc phyn rwri"
#             )
        
#         else:
#             print("Not available yet")
