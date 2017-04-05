#! python3
# incidentParser.py - parses incident data from the Boca Police Department and cleans it up.

import re
import csv

raw_incident_file = "bocaIncidents.csv"
headers = ['type', 'date', 'address'];

def main():
    parse_rows();
    write_new_file();
    print(*parsed_rows, sep='\n')


parsed_rows = []

def parse_rows():
    with open(raw_incident_file) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            crime_type = row[0]
            # Remove incident number with regex
            if row[2] == '':
                row[1] = re.sub('\d{10}', '', row[1]);
                crime_date = row[1].split(',')[0];
                crime_year = row[1].split()[2];
                crime_address = re.sub('^.+?\d{4}', '', row[1]);
                crime_address = crime_address.title().strip() + ', Boca Raton, Florida'
            else:
                row[1] = re.sub('\d{10}', '', row[1]);
                crime_date = row[1].split(',')[0];
                crime_year = row[1].split()[2];
                crime_address = row[2];
                crime_address = crime_address.title().strip() + ', Boca Raton, Florida'                
            parsed_rows.append([crime_type, crime_date + ', ' + crime_year, crime_address])

def write_new_file():
    with open('boca-incidents-final.csv', 'w', newline='') as finalfile:
            writer = csv.writer(finalfile)
            writer.writerow(headers)
            writer.writerows(parsed_rows)
    

if __name__ == "__main__":
    print("Cleaning file now...");
    main();
    print("All done!");