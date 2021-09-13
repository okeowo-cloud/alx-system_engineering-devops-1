#!/usr/bin/python3
"""
a script that
returns information about his/her TODO list progress.
"""
import json
import requests


def todo_all_employees():
    """ returns information about his/her TODO list progress. """
    user = (requests.get(
        'http://jsonplaceholder.typicode.com/users')).json()
    res = (requests.get(
        'https://jsonplaceholder.typicode.com/todos')).json()

    to_json = {}

    for userId in range(10):
        tasks = []
        username = user[userId].get('username')
        for todo in res:
            if todo.get('userId') == userId + 1:
                dic_todo = {}
                dic_todo['task'] = todo.get('title')
                dic_todo['completed'] = todo.get('completed')
                dic_todo['username'] = username
                tasks.append(dic_todo)
        to_json[userId + 1] = tasks
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(to_json, f, sort_keys=True)


if __name__ == '__main__':
    todo_all_employees()
