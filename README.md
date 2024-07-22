# Ko-Fi Scrapper

Ko-Fi Scrapper is a Python script that scrapes items from a Ko-Fi shop and sends the details to a Discord webhook. The script is designed to run continuously, checking for new items every minute and notifying a Discord channel when new items are found.

## Features

- Scrapes items from a specified Ko-Fi shop URL.
- Extracts item details such as name, image, tags, description, and price.
- Sends item details to a Discord webhook.
- Runs in headless mode using Selenium.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Zalgoo/Ko-Fi-Scrapper.git
    cd Ko-Fi-Scrapper
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Configure the script:
    - Set the `url` variable to the Ko-Fi shop URL you want to scrape.
    - Set the `discord_webhook_url` variable to your Discord webhook URL.
    - Optionally, adjust the `embed_color` variable to your desired embed color.

2. Run the script:
    ```bash
    python scraper.py
    ```

The script will start scraping the specified Ko-Fi shop and will send item details to the configured Discord webhook.

## Logging

The script uses the `logging` module to log information, errors, and debug messages. The logs are printed to the console.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by [Zalgoo](https://github.com/Zalgoo).
