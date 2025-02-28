#!/usr/bin/python3
"""python script that exports data in the JSON format"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    request_employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/".format(argv[1])
    )

    user = json.loads(request_employee.text)
    username = user.get("username")
    request_todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    )

    tasks = {}
    user_todos = json.loads(request_todos.text)

    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    task_list = []
    for k, v in tasks.items():
        task_list.append({"task": k, "completed": v, "username": username})

    json_to_dump = {argv[1]: task_list}
    with open("{}.json".format(argv[1]), mode="w") as file:
        json.dump(json_to_dump, file)
