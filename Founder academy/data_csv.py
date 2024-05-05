import csv

headers = ['CompanyName', 'PhoneNumber', 'Website']

data = [
    ['Nile United', '+201007000849', 'http://www.nileunited.com'],
]

filename = 'data.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)

