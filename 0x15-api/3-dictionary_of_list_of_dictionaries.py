#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests

if __name__ == '__main__':
    json_file = "todo_all_employees.json"
    end_point_1 = "https://jsonplaceholder.typicode.com/users"
    end_point_2 = "https://jsonplaceholder.typicode.com/todos"

    response_1 = requests.get(end_point_1)

    users = response_1.json()
    all_employees = {}

    for user in users:
        username = user['username']
        user_id = user['id']
        payload = {'userId': user_id}
        response_2 = requests.get(end_point_2, params=payload)
        todos = response_2.json()
        all_tasks = [{"username": username,
                      "task": todo['title'],
                      "completed": todo['completed']} for todo in todos]
        user_tasks = {user_id: all_tasks}
        all_employees[user_id] = all_tasks
    json_obj = json.dumps(all_employees)

    with open(json_file, 'w') as file:
        file.write(json_obj)
