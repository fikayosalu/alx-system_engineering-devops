#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries module"""
import json
import requests


def fetch_and_export_all_json():
    url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_response = requests.get(f"{url}/users")
    users = users_response.json()

    # Fetch all todos
    todos_response = requests.get(f"{url}/todos")
    todos = todos_response.json()

    # Dictionary to store all tasks grouped by user ID
    all_tasks = {}

    # Create a dictionary mapping user IDs to usernames
    user_dict = {user["id"]: user.get("username", "Unknown") for user in users}

    # Organize todos under respective users
    for task in todos:
        user_id = task.get("userId")
        if user_id not in all_tasks:
            all_tasks[user_id] = []

        all_tasks[user_id].append({
            "username": user_dict.get(user_id, "Unknown"),
            "task": task.get("title", "No Title"),
            "completed": task.get("completed", False)
        })

    # Define JSON file name
    file_name = "todo_all_employees.json"

    # Write to JSON file
    with open(file_name, mode="w") as json_file:
        json.dump(all_tasks, json_file)

    print(f"Data exported successfully to {file_name}")


# Run the function
if __name__ == "__main__":
    fetch_and_export_all_json()
