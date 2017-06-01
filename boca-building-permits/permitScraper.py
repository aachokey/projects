import csv
import requests
import re
from bs4 import BeautifulSoup

# url = input("Enter a url: ")
# Applied permits: http://apps.ci.boca-raton.fl.us/bp/applied-permits.php
# Issued permits: http://apps.ci.boca-raton.fl.us/bp/issued-permits.php

url = "http://apps.ci.boca-raton.fl.us/bp/issued-permits.php"

link_list = []

def main():
    get_files();


def get_files():
    r = requests.get(url)
    if int(r.status_code) == 200:

        print("Scraping page...")
        soup = BeautifulSoup(r.content, "html5lib");
        page_links = soup.select('a[href]');

        for link in page_links:
            if 'xls' in link.text.strip().lower():

    else:
        print("That URL doesn't work.")

        


if __name__ == "__main__":
    main();
    print("All done!");