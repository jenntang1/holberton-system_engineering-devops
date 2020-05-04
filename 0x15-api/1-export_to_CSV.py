#!/usr/bin/python3
""" Exports data into CSV format """


import csv
import requests
import sys


if isinstance(sys.argv[1], int) is True:
    user_id = sys.argv[1]
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    tasks_data = requests.get(tasks_url)

    with open('{}.csv'.format(user_id), 'w') as csv_file:
        tasks_writer = csv.writer(csv_file, delimiter=',',
                                  quotechar='"',
                                  quoting=csv.QUOTE_ALL)
        tasks_writer.writerow(tasks_data)
