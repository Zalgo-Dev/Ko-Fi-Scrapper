import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import time
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration parameters
url = 'https://ko-fi.com/example/shop'  # Shop page URL
discord_webhook_url = 'https://discord.com/api/webhooks/'  # Discord webhook URL
embed_color = 0x3498db  # Embed color in hexadecimal

# File to store retrieved items
items_file = 'items.json'

# Configure Selenium to run in headless mode
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)  # Ensure the path to ChromeDriver is set in your PATH

# Function to load retrieved items
def load_items():
    try:
        with open(items_file, 'r') as f:
            content = f.read().strip()
            if not content:
                logging.info("items.json file is empty. Initializing new content.")
                return {}
            logging.info("Loading items from the file.")
            return json.loads(content)
    except FileNotFoundError:
        logging.info("items.json file not found. Creating a new file.")
        return {}
    except json.JSONDecodeError:
        logging.error("JSON decoding error. Initializing new content.")
        return {}

# Function to save retrieved items
def save_items(items):
    with open(items_file, 'w') as f:
        logging.info("Saving items to the file.")
        json.dump(items, f, indent=4)

# Function to send a message to Discord
def send_to_discord(item_url, name, img, tags, desc, price):
    data = {
        "content": "@everyone",
        "embeds": [
            {
                "title": name,
                "url": f"https://ko-fi.com{item_url}",
                "color": embed_color,
                "image": {"url": img},
                "fields": [
                    {"name": "Tags", "value": tags, "inline": False},
                    {"name": "Description", "value": desc, "inline": False},
                    {"name": "Price", "value": price, "inline": False}
                ]
            }
        ]
    }
    logging.info(f"Sending item to Discord: {item_url}")
    response = requests.post(discord_webhook_url, json=data)
    logging.info(f"Response status: {response.status_code}")
    if response.status_code == 204:
        logging.info(f"Message sent for item: {item_url}")
    else:
        logging.error(f"Error sending message for item: {item_url}")
        logging.error(f"Response: {response.text}")

# Function to extract item details
def get_item_details(item_url):
    logging.info(f"Retrieving item details: {item_url}")
    driver.get(f"https://ko-fi.com{item_url}")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.kfds-c-carousel-product-img')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    name_tag = soup.find('span', class_='shop-item-title kfds-font-size-22 kfds-font-bold break-long-words')
    name = name_tag.text.strip() if name_tag else 'Unnamed'
    logging.info(f"Name found: {name}")

    img_tag = soup.find('img', class_='kfds-c-carousel-product-img')
    img = img_tag['src'] if img_tag else ''
    logging.info(f"Image found: {img}")

    tags_li = soup.find_all('li', class_='kfds-lyt-between kfds-font-size-hint')
    tags = ""
    for li in tags_li:
        span = li.find('span')
        if span and "sold" not in span.text:
            tags = span.text.strip()
            break
    logging.info(f"Tags found: {tags}")

    desc_div = soup.find('div', class_='kfds-c-product-detail-res-width')
    desc = desc_div.find('p', class_='line-breaks kfds-c-word-wrap').text.strip() if desc_div and desc_div.find('p', class_='line-breaks kfds-c-word-wrap') else ''
    logging.info(f"Description found: {desc}")

    price_span = soup.find('span', class_='kfds-font-size-24 kfds-font-bold')
    price = price_span.text.strip() if price_span else ''
    logging.info(f"Price found: {price}")

    return name, img, tags, desc, price

# Initialize the items.json file if it does not exist
if not os.path.exists(items_file):
    logging.info(f"The file {items_file} does not exist. Creating a new file.")
    with open(items_file, 'w') as f:
        json.dump({}, f)

# Load already retrieved items
items = load_items()

def check_for_new_items():
    global items
    logging.info("Checking for new items.")
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.kfds-c-shop-item')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all item links in the shop
    item_links = soup.find_all('a', class_='kfds-c-shop-item')
    logging.info(f"{len(item_links)} items found in the shop.")

    new_items_found = False

    for link in item_links:
        item_url = link.get('href')
        if item_url and item_url not in items:
            logging.info(f"New item found: {item_url}")
            # If the item has never been retrieved, extract details, send to Discord, and add to the list
            name, img, tags, desc, price = get_item_details(item_url)
            logging.info(f"Item details: name={name}, img={img}, tags={tags}, desc={desc}, price={price}")
            send_to_discord(item_url, name, img, tags, desc, price)
            items[item_url] = {
                "name": name,
                "img": img,
                "tags": tags,
                "desc": desc,
                "price": price
            }
            new_items_found = True
            # Pause to avoid overloading the server with rapid requests
            time.sleep(2)
    
    if new_items_found:
        # Save the updated list of retrieved items
        save_items(items)
    else:
        logging.info("No new items found.")

# Perform an initial scan
check_for_new_items()

# Infinite loop to check for new items every minute
while True:
    logging.info("Waiting for 60 seconds before the next check...")
    time.sleep(60)
    check_for_new_items()
