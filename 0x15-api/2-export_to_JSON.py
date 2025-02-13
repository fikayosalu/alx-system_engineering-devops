#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_response = requests.get(f'https://jsonplaceholder\
.typicode.com/users/{user_id}')
    task_response = requests.get(f'https://jsonplaceholder\
.typicode.com/users/{user_id}/todos')
    user = user_response.json()
    task = task_response.json()
    done_task = [item for item in task if item.get('completed')]

    with open(f"{user_id}.json", mode="w", newline="") as file:
        data = []
        for items in task:
            data.append({
                "task": f"{items.get('title')}",
                "completed": f"{items.get('completed')}",
                "username": user.get('username')
            })
        user_record = {f"{user_id}": data}

        file.write(json.dumps(user_record))
