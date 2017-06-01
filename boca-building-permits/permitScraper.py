import csv
import requests
import re
from bs4 import BeautifulSoup

url = input("Enter a url: ")
# Applied permits: http://www.myboca.us/0122/Applied-Permits
# Issued permits: http://www.myboca.us/1123/Issued-Permits


def main():
	get_files();


def get_files():
	r = requests.get(url)
	if r.status_code == 200:
		pass
	else:
		print("That URL doesn't work.")
	print("Scraping permits...");
	soup = BeautifulSoup(r.content, "html5lib");
	print(r.content)






if __name__ == "__main__":
	main();
	print("All done!");