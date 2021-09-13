#!/usr/bin/python3
"""
a script that
returns information about his/her TODO list progress.
"""
import requests
from sys import argv
import csv


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
        with open('USER_ID.csv', mode='a') as todo_file:
            todo_writer = csv.writer(
                todo_file,
                delimiter=',',
                quoting=csv.QUOTE_ALL)
            todo_writer.writerow([todo.get('userId'), user[0].get('username'),
                                  todo.get('completed'), todo.get('title')])


if __name__ == '__main__':
    getText()
