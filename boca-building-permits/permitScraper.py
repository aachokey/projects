import csv
import requests
import re
from bs4 import BeautifulSoup

# url = input("Enter a url: ")
# Applied permits: http://apps.ci.boca-raton.fl.us/bp/applied-permits.php
# Issued permits: http://apps.ci.boca-raton.fl.us/bp/issued-permits.php

url = "http://apps.ci.boca-raton.fl.us/bp/issued-permits.php"
output_file = input("What do you want to call this file? (Don't add extension): ");

link_list = []

def main():
    lookup_files();
    # scrape_files();


def lookup_files():
    r = requests.get(url)
    if int(r.status_code) == 200:

        print("Scraping page...")
        soup = BeautifulSoup(r.content, "html5lib");
        page_links = soup.select('a[href]');

        for link in page_links:
            # if 'xls' in link.text.strip().lower():
            print(link)
    else:
        print("That URL doesn't work.")

 
 # def scrape_files():
 #    print(link_list)


if __name__ == "__main__":
    main();
    print("All done!");