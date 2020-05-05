#!/usr/bin/python3
""" Exports data into CSV format """


import csv
import requests
import sys


if __name__ == "__main__":
    """ If second argument is an integer, then it's an employee id """
    empl_id = sys.argv[1]
    if empl_id.isdigit():

        """ Gets EMPLOYEE_NAME """
        empl_url = "https://jsonplaceholder.typicode.com/users/{}".\
            format(empl_id)
        response = requests.get(empl_url)
        empl_name = response.json().get("name")
        username = response.json().get("username")

        """ Gets tasks assigned to employee """
        tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos".\
            format(empl_id)
        response = requests.get(tasks_url)
        todos = response.json()

        """ Gets NUMBER_OF_DONE_TASKS """
        tasks_done = 0
        tasks_list = []
        for key in todos:
            if key["completed"] is True:
                tasks_done += 1
                tasks_list.append(key["title"])

        """ Gets TOTAL_NUMBER_OF_TASKS """
        tasks_total = 0
        for key in todos:
            if key["title"]:
                tasks_total += 1
        print("Employee {} is done with tasks({}/{}):".format(empl_name,
                                                              tasks_done,
                                                              tasks_total))

        """ Gets TASK_TITLE """
        for element in tasks_list:
            print("\t {}".format(element))

        """ Adds username to the todos data """
        todos_list = list(todos)
        name_pair = {"username": username}
        for dicts in todos_list:
            dicts.update(name_pair)

        """ Exports to CSV """
        with open("{}.csv".format(empl_id), "w") as csv_file:
            columns = ["userId", "username", "completed", "title"]
            tasks_writer = csv.DictWriter(csv_file,
                                          delimiter=",",
                                          quotechar='"',
                                          quoting=csv.QUOTE_ALL,
                                          fieldnames=columns,
                                          extrasaction="ignore")
            todos_dict = {}
            for dicts in todos_list:
                todos_dict.update(dicts)
                tasks_writer.writerow(todos_dict)
