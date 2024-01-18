# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 18:43:05 2024

@author: Dobby
"""

from bs4 import BeautifulSoup
import requests
import re

class WebScraper:
    def __init__(self, category=82105, max_pages=9):
        self.category = category
        self.max_pages = max_pages

    def scrape_data(self):
        for i in range(1, self.max_pages + 1):
            response = requests.get(f"https://www.yep.co.za/search?category={self.category}&pageNumber={i}")
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            # Use find_all, not findall
            names = soup.find_all('h6', class_="text-1-liner lh-normal")
            addresses = soup.find_all('p', class_="text-2-liner location_location_name__j8wyE")

            for i in range(len(names)):
                name = names[i]
                address = addresses[i]

                self.print_store_info(name, address)

    def print_store_info(self, name, address):
        print("Store name:", name.text)
        pattern = r",\s*([^,]+)\s*(\d{4}),\s*([^,]+)$"

        # Use re.search to find the match in the address string
        match = re.search(pattern, address.text)  # Use address.text

        # Check if the pattern is found and extract the city and province
        if match:
            city = match.group(1)  # Group 1 corresponds to the city
            province = match.group(3)  # Group 3 corresponds to the province

            print("City:", city)
            print("Province:", province)
        else:
            print("Pattern not found in the address string.")
        print("")

# Create an instance of WebScraper and run the script
scraper = WebScraper()
scraper.scrape_data()
