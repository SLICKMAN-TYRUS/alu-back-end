#!/usr/bin/python3
"""Module"""

import json
import requests


def get_employee_task(employee_id):
    """Doc"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    user_info = requests.request("GET", user_url).json()

    employee_username = user_info["username"]
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        employee_id
    )
    todos_info = requests.request("GET", todos_url).json()
    return [
        dict(
            zip(
                ["task", "completed", "username"],
                [task["title"], task["completed"], employee_username],
            )
        )
        for task in todos_info
    ]


def get_employee_ids():
    """Doc"""
    users_url = "https://jsonplaceholder.typicode.com/users/"

    users_info = requests.request("GET", users_url).json()
    ids = list(map(lambda user: user["id"], users_info))
    return ids


if __name__ == "__main__":
    employee_ids = get_employee_ids()

    with open("todo_all_employees.json", "w") as file:
        all_users = {}
        for employee_id in employee_ids:
            all_users[str(employee_id)] = get_employee_task(employee_id)
        file.write(json.dumps(all_users))
