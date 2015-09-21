# Caroline Azeau
# 10334858

# Programm to change the CSV data into JSON data0

import csv
import json

csvfile = open( 'KNMI_data_csv.csv', 'r' )
jsonfile = open( 'KNMI_data_json.json', 'w')

data = []
for i in csvfile:
    a = i.strip()
    b = a.split( "," )
    b[1]=int(b[1])
    data.append(b)

json.dump(data,jsonfile)
