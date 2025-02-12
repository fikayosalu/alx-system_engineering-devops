#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user_response = requests.get(f'https://jsonplaceholder\
.typicode.com/users/{id}')
    task_response = requests.get(f'https://jsonplaceholder\
.typicode.com/users/{id}/todos')
    user = user_response.json()
    task = task_response.json()
    done_task = [item for item in task if item.get('completed')]

    print(f"Employee {user.get('name')} is \
done with tasks({len(done_task)}/{len(task)}):")

    for item in done_task:
        print(f"\t {item.get('title')}")
