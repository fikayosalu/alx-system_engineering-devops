#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import csv
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

    with open(f"{user_id}.csv", mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for items in task:
            writer.writerow([
                user_id,
                user.get('username'),
                items.get('completed'),
                items.get('title')
            ])
