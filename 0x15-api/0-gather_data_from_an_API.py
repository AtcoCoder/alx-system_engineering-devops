#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    payload = {'userId': userId}
    end_point1 = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    end_point_2 = "https://jsonplaceholder.typicode.com/todos"

    response_1 = requests.get(end_point1)
    response_2 = requests.get(end_point_2, params=payload)

    user = response_1.json()
    todos = response_2.json()

    name = user['name']

    n_tasks = len(todos)
    tasks_done = [todo['title'] for todo in todos if todo['completed'] is True]
    done = len(tasks_done)

    print("Employee {} is done with tasks({}/{}):".format(name, done, n_tasks))
    for todo in tasks_done:
        print('\t {}'.format(todo))
