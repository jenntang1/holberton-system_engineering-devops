#!/usr/bin/python3
""" Exports data into JSON format """


import json
import requests
import sys


if __name__ == "__main__":

    """ Gets length of list of employees """
    empl_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(empl_url)
    length = len(response.json())

    todos_dict = {}
    for empl_id in range(1, length + 1):
        """ Gets all username """
        empl_url = "https://jsonplaceholder.typicode.com/users/{}".\
            format(empl_id)
        response = requests.get(empl_url)
        username = response.json()["username"]

        """ Gets all tasks """
        tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos".\
            format(empl_id)
        response = requests.get(tasks_url)
        todos = response.json()

        """ Adds username to todos data """
        todos_list = list(todos)
        name_pair = {"username": username}
        for dicts in todos_list:
            dicts.update(name_pair)

        """ Reformats todos data """
        for item in todos_list:
            del item["id"]
            del item["userId"]
            item["task"] = item.pop("title")

        """ Sets USER_ID as key and todos data as a list of values """
        todos_dict[empl_id] = todos_list

    """ Exports to JSON """
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todos_dict, json_file)
