#!/usr/bin/python3
"""1-export_to_CSV module"""
import csv
import requests
import sys


def fetch_and_export_csv(employee_id):
    url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_response = requests.get(f"{url}/todos/{employee_id}")
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    user_data = user_response.json()
    print(user_data)
    employee_username = user_data.get("name", "Antonette")  # Using .get()

    # Fetch employee's todo list
    todos_response = requests.get(f"{url}/todos?userId={employee_id}")
    todos = todos_response.json()

    # Define CSV file name
    file_name = f"{employee_id}.csv"

    # Write to CSV file
    with open(file_name, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow([
                employee_id,
                employee_username,
                task.get("completed"),  # Using .get()
                task.get("title", "No Title")  # Using .get()
            ])

    print(f"Data exported successfully to {file_name}")


# Ensure the script is run with an employee ID argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python export_to_csv.py <employee_id>")
    else:
        try:
            emp_id = int(sys.argv[1])  # Convert argument to integer
            fetch_and_export_csv(emp_id)
        except ValueError:
            print("Employee ID must be an integer.")
