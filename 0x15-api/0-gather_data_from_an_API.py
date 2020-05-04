#!/usr/bin/python3
""" Gather task data based on employee id from an API """


import requests
import sys


if __name__ == "__main__":
    """ If second argument is an integer, then it's an employee id """
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
        completed = response.json()
        """ Get NUMBER_OF_DONE_TASKS """
        tasks_done = 0
        tasks_list = []
        for key in completed:
            if key["completed"] is True:
                tasks_done += 1
                tasks_list.append(key["title"])
        """ Get TOTAL_NUMBER_OF_TASKS """
        tasks_total = 0
        for key in completed:
            if key["title"]:
                tasks_total += 1
        print("Employee {} is done with tasks({}/{}):".format(empl_name,
                                                              tasks_done,
                                                              tasks_total))
        """ Get TASK_TITLE """
        for element in tasks_list:
            print("\t {}".format(element))
