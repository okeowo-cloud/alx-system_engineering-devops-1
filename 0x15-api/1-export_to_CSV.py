#!/usr/bin/python3
"""
a script that
returns information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv


def export_to_csv():
    """ returns information about his/her TODO list progress. """
    user = (requests.get(
        'http://jsonplaceholder.typicode.com/users?id={}'.format(
            argv[1]))).json()
    res = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    done_task = []
    num_all_task = 0
    num_done_task = 0
    userId = user[0].get('id')
    for todo in res.json():
        with open('{}.csv'.format(userId), mode='a') as todo_file:
            todo_writer = csv.writer(
                todo_file,
                quoting=csv.QUOTE_ALL)
            todo_writer.writerow([userId, user[0].get('username'),
                                  todo.get('completed'), todo.get('title')])


if __name__ == '__main__':
    export_to_csv()
