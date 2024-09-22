import csv

headers = ['PhoneNumber', 'CompanyName', 'Website']

data = [
     {'Nile United', '+201007000849', 'http://www.nileunited.com' },
     {'Roqay', '', 'https://roqay.com/'},
     {'wajz information technology ', '', 'www.wajz.sa'},
     {'Digital business system', '', 'https://www.dbsmena.com'},
     {'Boubyan digital factory ', '', 'https://boubyan.bankboubyan.com/en/boubyan-digital-factory/'},
     {'Lavaloon', '', 'Lavaloon.com'},
     {'Datenlotsen ', '', 'https://www.datenlotsen.de/en/'},
     {'Awamer Elshabaka', '', 'https://aait.sa/'},
     {'البدر للنظم الذكية', '', 'https://albadrsystems.com/ar/'},
     {'Quarizm', '', 'https://quarizm.tech/'},
     # Quarizm is remotly and don't have a site
     {'serv5 web solutions', '', 'serv5.com.eg'},
]

filename = 'data.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)

