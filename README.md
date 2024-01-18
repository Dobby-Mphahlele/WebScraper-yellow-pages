# WebScraper-yellow-pages
Python Script for Web Scraping and  Automation

Web Scraper for [Yep.co.za](https://www.yep.co.za/search?category=82105&pageNumber=1)
## Overview
This Python script is a web scraper designed to extract information from the Yep.co.za website related to a specific category and across multiple pages. It utilizes the BeautifulSoup library for HTML parsing and requests library to make HTTP requests.

## Features
**Customization:** The script allows customization of the category and the maximum number of pages to scrape. <br />
**Data Extraction:** It extracts campany names, cities, and provinces from the specified web pages.

## How to Use
Installation:
> [!TIP]
> Ensure you have Python installed on your system.
> Install the required Python packages using the following command:
 ```
 pip install requests beautifulsoup4
```
### Run the Script:
Save the script to a file, e.g., web_scraper.py.
Open a terminal or command prompt.
Navigate to the directory containing the script.
Run the script using the following command:
```
python web_scraper.py
```
Customization:<br/>
You can customize the script by modifying the category and max_pages parameters in the WebScraper class constructor.

# Dependencies
**Requests:**
Used for making HTTP requests to the Yep.co.za website.<br/>
Install using:
```
pip install requests
```

> [!CAUTION]
> Respect Website Policies:
> Before running the script, ensure compliance with the terms of service of the [Yep.co.za](https://www.yep.co.za/search?category=82105&pageNumber=1) website. Check the website's robots.txt file for any scraping guidelines.

> [!TIP]
> Continuous Execution:<br/>
> The script is designed to run continuously, with a delay of 7 days between each execution. Consider the potential impact on the server and adhere to any rate-limiting guidelines.
Dataset Updates:

The script is intended to keep the dataset up-to-date by periodically scraping data from the specified web pages.

Author<br/>
Dobby. M

