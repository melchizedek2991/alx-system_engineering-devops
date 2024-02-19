0x15. api
0x15-api/0-gather_data_from_an_API.py


#!/usr/bin/python3

"""

Returns to-do list information for a given employee ID.


This script takes an employee ID as a command-line argument and fetches

the corresponding user information and to-do list from the JSONPlaceholder API.

It then prints the tasks completed by the employee.

"""


import requests

import sys



if __name__ == "__main__":

    # Base URL for the JSONPlaceholder API

    url = "https://jsonplaceholder.typicode.com/"


    # Get the employee information using the provided employee ID

    employee_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(employee_id)).json()


    # Get the to-do list for the employee using the provided employee ID

    params = {"userId": employee_id}

    todos = requests.get(url + "todos", params).json()


    # Filter completed tasks and count them

    completed = [t.get("title") for t in todos if t.get("completed") is True]


    # Print the employee's name and the number of completed tasks

    print("Employee {} is done with tasks({}/{}):".format(

        user.get("name"), len(completed), len(todos)))


    # Print the completed tasks one by one with indentation

    [print("\t {}".format(complete)) for complete in completed]



0x15-api/1-export_to_CSV.py


#!/usr/bin/python3

"""Exports to-do list information for a given employee ID to CSV format."""


import csv

import requests

import sys



if __name__ == "__main__":

    # Get the user ID from the command-line arguments provided to the script

    user_id = sys.argv[1]


    # Define the base URL for the JSON API

    url = "https://jsonplaceholder.typicode.com/"


    # Fetch user information from the API and

    #   convert the response to a JSON object

    user = requests.get(url + "users/{}".format(user_id)).json()


    # Extract the username from the user data

    username = user.get("username")


    # Fetch the to-do list items associated with the

    #   given user ID and convert the response to a JSON object

    todos = requests.get(url + "todos", params={"userId": user_id}).json()


    # Use list comprehension to iterate over the to-do list items

    # Write each item's details (user ID, username, completion status,

    #   and title) as a row in the CSV file

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:

        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        [writer.writerow(

            [user_id, username, t.get("completed"), t.get("title")]

         ) for t in todos]



0x15-api/2-export_to_JSON.py


#!/usr/bin/python3

"""

Exports to-do list information for a given employee ID to JSON format.


This script takes an employee ID as a command-line argument and exports

the corresponding user information and to-do list to a JSON file.

"""


import json

import requests

import sys



if __name__ == "__main__":

    # Get the employee ID from the command-line argument

    user_id = sys.argv[1]


    # Base URL for the JSONPlaceholder API

    url = "https://jsonplaceholder.typicode.com/"


    # Fetch user information using the provided employee ID

    user = requests.get(url + "users/{}".format(user_id)).json()

    username = user.get("username")


    # Fetch the to-do list for the employee using the provided employee ID

    params = {"userId": user_id}

    todos = requests.get(url + "todos", params).json()


    # Create a dictionary containing the user and to-do list information

    data_to_export = {

        user_id: [

            {

                "task": t.get("title"),

                "completed": t.get("completed"),

                "username": username

            }

            for t in todos

        ]

    }


    # Write the data to a JSON file with the employee ID as the filename

    with open("{}.json".format(user_id), "w") as jsonfile:

        json.dump(data_to_export, jsonfile, indent=4)
