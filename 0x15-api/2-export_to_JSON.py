#!/usr/bin/python3
"""2-export_to_JSON"""
import json
import requests
import sys


def fetch_and_export_json(employee_id):
    url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_response = requests.get(f"{url}/todos/{employee_id}")
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    user_data = user_response.json()
    employee_username = user_data.get("username", "Unknown")  # Using .get()

    # Fetch employee's todo list
    todos_response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = todos_response.json()

    # Create JSON structure
    task_list = [
        {
            "task": task.get("title", "No Title"),
            "completed": task.get("completed", False),
            "username": employee_username
        }
        for task in todos
    ]

    json_data = {str(employee_id): task_list}

    # Define JSON file name
    file_name = f"{employee_id}.json"

    # Write to JSON file
    with open(file_name, mode="w") as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported successfully to {file_name}")


# Ensure the script is run with an employee ID argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python export_to_json.py <employee_id>")
    else:
        try:
            emp_id = int(sys.argv[1])  # Convert argument to integer
            fetch_and_export_json(emp_id)
        except ValueError:
            print("Employee ID must be an integer.")
