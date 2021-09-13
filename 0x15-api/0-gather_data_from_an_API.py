#!/usr/bin/python3
"""
a script that
returns information about his/her TODO list progress.
"""
import requests
from sys import argv
import json


def getText():
    """ returns information about his/her TODO list progress. """
    user = (requests.get(
        'http://jsonplaceholder.typicode.com/users?id={}'.format(
            argv[1]))).json()
    res = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    done_task = []
    num_all_task = 0
    num_done_task = 0
    for todo in res.json():
        if todo['completed']:
            num_done_task += 1
            done_task.append(todo['title'])
        num_all_task += 1
    print("Employee {} is done with tasks({:d}/{:d}):".format(
        user[0]['name'], num_done_task, num_all_task))
    for i in done_task:
        print("\t {}".format(i))


if __name__ == '__main__':
    getText()