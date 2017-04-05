#! python3
# incidentParser.py - parses incident data from the Boca Police Department.

import re
import csv

incident_file = "bocaIncidents.csv"


def main():
    parse_rows()
    # save_new_file()


def parse_rows():
    with open(incident_file) as csvfile:
        csvreader = csv.reader(csvfile, quotechar='|')
        parsed_rows = []
        for row in csvreader:
            crime_type = row[0]
            # Remove incident number
            crime_date = re.sub('\d{10}', '', row[1]);
            crime_date = crime_date.replace('"', '') + ', '
            crime_year = row[2].split()[0];
            crime_address = re.sub('^.+?\s', '', row[2]);
            crime_address = crime_address.title().replace('"', '') + ', Boca Raton, Florida'
            parsed_rows.append([crime_type, crime_date + crime_year, crime_address])
        write_new_file(parsed_rows)


def write_new_file(iterable):
    with open('boca-incidents-final.csv', 'w', newline='') as finalfile:
            writer = csv.writer(finalfile)
            writer.writerows(iterable)
    

if __name__ == "__main__":
    # This function executes when you do "filingScraper.py" on the command line.
    print("Cleaning file now...");
    main();
    print("All done!");