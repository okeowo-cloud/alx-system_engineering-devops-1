#!/usr/bin/python3
"""
a script that
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


def export_to_json():
    """ returns information about his/her TODO list progress. """
    user = (requests.get(
        'http://jsonplaceholder.typicode.com/users?id={}'.format(
            argv[1]))).json()
    res = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    tasks = []
    to_json = {}
    userId = user[0].get('id')
    username = user[0].get('username')
    for todo in res.json():
        dic_todo = {}
        dic_todo['task'] = todo.get('title')
        dic_todo['completed'] = todo.get('completed')
        dic_todo['username'] = username
        tasks.append(dic_todo)
    to_json[userId] = tasks
    with open('{}.json'.format(userId), 'w') as todo_file:
        json.dump(to_json, todo_file)


if __name__ == '__main__':
    export_to_json()
