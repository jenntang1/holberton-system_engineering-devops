#!/usr/bin/python3
""" Exports data into CSV format """


import csv
import requests
import sys


if __name__ == "__main__":
    """ If second argument is an integer, then it's an employee id """
    run_script = sys.argv[0]
    empl_id = sys.argv[1]
    if empl_id.isdigit():

        """ Get EMPLOYEE_NAME """
        empl_url = "https://jsonplaceholder.typicode.com/users/{}".\
            format(empl_id)
        response = requests.get(empl_url)
        empl_name = response.json().get("name")

        """ Get tasks assigned to employee """
        tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos".\
            format(empl_id)
        response = requests.get(tasks_url)
        todos = response.json()

        """ Get NUMBER_OF_DONE_TASKS """
        tasks_done = 0
        tasks_list = []
        for key in todos:
            if key["completed"] is True:
                tasks_done += 1
                tasks_list.append(key["title"])

        """ Get TOTAL_NUMBER_OF_TASKS """
        tasks_total = 0
        for key in todos:
            if key["title"]:
                tasks_total += 1

        """ Print data to standard out """
        if run_script == "0-gather_data_from_an_API.py":
            print("Employee {} is done with tasks({}/{}):".format(empl_name,
                                                                  tasks_done,
                                                                  tasks_total))

            for element in tasks_list:
                print("\t {}".format(element))

        else:
            """ Exports to CSV """
            with open("{}.csv".format(empl_id), "w") as csv_file:
                columns = ["userId", "id", "completed", "title"]
                tasks_writer = csv.DictWriter(csv_file,
                                              delimiter=",",
                                              quotechar='"',
                                              quoting=csv.QUOTE_ALL,
                                              fieldnames=columns)
                todos_dict = {}
                for dicts in todos:
                    todos_dict.update(dicts)
                    tasks_writer.writerow(todos_dict)
