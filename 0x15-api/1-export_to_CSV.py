#!/usr/bin/python3
"""Gather data from an API"""
import requests
import csv
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    csv_file = "{}.csv".format(userId)
    payload = {'userId': userId}
    end_point1 = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    end_point_2 = "https://jsonplaceholder.typicode.com/todos"

    response_1 = requests.get(end_point1)
    response_2 = requests.get(end_point_2, params=payload)

    user = response_1.json()
    todos = response_2.json()

    name = user['name']

    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        for todo in todos:
            title = todo['title']
            task_status = todo['completed']
            row = [userId, name, task_status, title]
            writer.writerow(row)
