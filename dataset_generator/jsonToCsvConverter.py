import json
import csv
import requests

# Opening JSON file and loading the data 
# into the variable data 
# with open('data.json') as json_file:
#     data = json.load(json_file)
#
# employee_data = data['emp_details']
#
# # now we will open a file for writing
# data_file = open('data_file.csv', 'w')
#
# # create the csv writer object
# csv_writer = csv.writer(data_file)
#
# # Counter variable used for writing
# # headers to the CSV file
# count = 0
#
# for emp in employee_data:
#     if count == 0:
#
#         # Writing headers of CSV file
#         header = emp.keys()
#         csv_writer.writerow(header)
#         count += 1
#
#     # Writing data of CSV file
#     csv_writer.writerow(emp.values())
#
# data_file.close()

api = 'https://api.tiingo.com/tiingo/daily/eth/prices?startDate=2012-1-1&endDate=2021-3-1&'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token e8f19de4f1014da0c82def9df3edf347cc139584'
}

eth_data = json.loads(requests.get(api, headers=headers).content.decode('utf-8'))

file = open('eth.csv', 'w')
csv_writer = csv.writer(file)

count = 0

for record in eth_data:
    if count == 0:

        # Writing headers of CSV file
        header = record.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(record.values())

file.close()
