import requests
import csv

import pandas as pd
from bs4 import BeautifulSoup


url = "http://apps.ci.boca-raton.fl.us/bp/issued-permits.php"
"http://apps.ci.boca-raton.fl.us/bp/applied-permits.php"

header_names = ["application-number","application-date","issued-date","app-type",
"application-type-description","work-desciption","estimated-value","property-address",
"property-addres2","tenant-name","owner-info1","owner-info2","owner-info3",
"owner-info4","owner-phone","contractor","contractor-phone"]

link_list = []

def main():
    lookup_files();
    download_files();


def lookup_files():
    r = requests.get(url)
    if int(r.status_code) == 200:

        print("Scraping links...")
        soup = BeautifulSoup(r.content, "html5lib");
        for link in soup.find_all('a'):
            link_url = link.get('href')
            link_list.append("http://apps.ci.boca-raton.fl.us%s" % link_url)
    else:
        print("That URL doesn't work.")
 
def download_files():
    print('Downloading ' + str(len(link_list)) + ' links.') 
    with open('data/boca-issued-permits.csv', 'w') as permitfile:
        writer = csv.writer(permitfile)
        writer.writerow(header_names)
        for file in link_list:
            xlsFile = pd.read_excel(file, index_col=None)
            xlsFile.to_csv(permitfile, header=False, index=False)


if __name__ == "__main__":
    main();
    print("All done!");