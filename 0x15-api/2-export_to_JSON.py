#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    json_file = "{}.json".format(userId)
    payload = {'userId': userId}
    end_point1 = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    end_point_2 = "https://jsonplaceholder.typicode.com/todos"

    response_1 = requests.get(end_point1)
    response_2 = requests.get(end_point_2, params=payload)

    user = response_1.json()
    todos = response_2.json()

    username = user['username']

    all_tasks = [{"task": todo['title'],
                  "completed": todo['completed'],
                  "username": username} for todo in todos]
    user_tasks = {userId: all_tasks}
    json_obj = json.dumps(user_tasks)

    with open(json_file, 'w') as file:
        file.write(json_obj)
