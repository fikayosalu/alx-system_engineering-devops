#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import requests
import sys


def fetch_employee_todo(employee_id):
    # Base URL of the REST API
    url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_response = requests.get(f"{url}/todos/{employee_id}")
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee's todo list
    todos_response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = todos_response.json()

    # Count completed tasks
    done_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)
    num_done_tasks = len(done_tasks)

    # Print result in the required format
    print(f"Employee {employee_name} is done with \
tasks({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")  # 1 tab and 1 space before title


# Ensure the script is run with an employee ID argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            emp_id = int(sys.argv[1])  # Convert argument to integer
            fetch_employee_todo(emp_id)
        except ValueError:
            print("Employee ID must be an integer.")
