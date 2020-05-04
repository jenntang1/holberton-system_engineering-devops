#!/usr/bin/python3
""" Gather task data based on employee id from an API """


import requests
import sys
import urllib


if __name__ == "__main__":

    if isinstance(sys.argv[1], int) is True:
        empl_id = sys.argv[1]
        empl_url = "https://jsonplaceholder.typicode.com/users"
        tasks_url = "https://jsonplaceholder.typicode.com/todos"
        empl_data = requests.get(empl_url)
        tasks_data = requests.get(tasks_url)

        if empl_id == empl_data.get("id"):
            empl_name = empl_data.get("name")

        for key in tasks_data:
            if empl_id == key.get("userID"):
                done_tasks = key.count("completed")
                total_tasks = key.count("title")
                task_title = key.get("title")
        print("Employee {} is done with tasks({}/{}):\n".format(empl_name, done_tasks, total_tasks))
        print("\t {}\n".format(task_title))
