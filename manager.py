import argparse
import json
import sys
import os


def create_admin(username, password):
    admin_file = "admin.json"

    manager_info = dict()
    manager_info["username"] = username
    manager_info["password"] = password

    data = json.load(open(admin_file, "r"))

    for item in data:
        if username == item.get("username"):
            print("Error: The system manager is already built.")
            return
    data.append(manager_info)
    with open(admin_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Admin '{username}' created successfully!")


def purge_data():
    response = input("Are you sure you want to purge all data? This action cannot be undone. (yes/no): ")

    if response.lower() != "yes":
        print("Data purge canceled.")
        return

    data_file = "admin.json"

    try:
        with open("admin.json", "r") as jsonFile:
            data = json.load(jsonFile)
            i = 0
            while len(data):
                data.pop(i)
                
        with open("admin.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)
                
        print("All data has been purged from admin file successfully.")
    except FileNotFoundError:
        print(f"Error: '{data_file}' not found.")
        
    data_file = "projects.json"

    try:
        with open("projects.json", "r") as jsonFile:
            data = json.load(jsonFile)
            i = 0
            while len(data):
                data.pop(i)
                
        with open("projects.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)
                
        print("All data has been purged from projects file successfully.")
    except FileNotFoundError:
        print(f"Error: '{data_file}' not found.")
        
    data_file = "users.json"

    try:
        with open("users.json", "r") as jsonFile:
            data = json.load(jsonFile)
            i = 0
            while len(data):
                data.pop(i)
                
        with open("users.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)
                
        print("All data has been purged from users file successfully.")
    except FileNotFoundError:
        print(f"Error: '{data_file}' not found.")


def main():
    parser = argparse.ArgumentParser(description="Create system administrator information")
    # print(parser)
    # exit(0)
    parser.add_argument("command", help="Command to execute")
    parser.add_argument("--username", help="Admin username")
    parser.add_argument("--password", help="Admin password")

    args = parser.parse_args()

    if args.command == "create-admin":
        create_admin(args.username, args.password)
    elif args.command == "purge-data":
        purge_data()


if __name__ == "__main__":
    main()
