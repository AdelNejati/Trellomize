from rich import console
import os
import json
import re
import uuid
import datetime
from enum import Enum

console = console.Console()


class Model:
    def __init__(self):
        self.id = uuid.uuid4()


class Account(Model):
    def __init__(self):
        self.id = Model()
        self.data = []
        self.user_info = dict()
        self.user_detail_list = []
        self.logged_in = False
        self.active_user_account = True
        self.user_info["ID"] = str(self.id)

    def register(self, user_name, password, email):
        self.user_info["gmail"] = email
        self.user_info["Username"] = user_name
        self.user_info["Password"] = password
        self.user_info["Is_active"] = "No" if not self.active_user_account else "Yes"
        self.data = json.load(open("users.json", "r"))

        def is_valid_gmail():
            pattern = r"^[A-Z|a-z][A-Z|a-z|0-9|\.|_|-]*@[\w|\d|_|-]+\.[\w]+$"
            if not re.fullmatch(pattern, email):
                console.print("Invalid gmail ! please enter valid gmail\n", style="bold red")
                return False
            return True

        def is_valid_username():
            if len(str(user_name)) < 3 or len(str(user_name)) > 14:
                console.print("Invalid userName ! please enter userName greater than 5 and less than 14 character\n",
                              style="bold red")
                return False
            elif any(user_name in item.get("Username") for item in self.data):
                console.print("Username is already used", style="bold red")
                return False
            return True

        def is_valid_password():
            if len(str(password)) < 5 or len(str(password)) > 18:
                console.print("Enter password greater than 5 and less than 18 character", style="bold red")
                return False
            return True

        if is_valid_username() and is_valid_gmail() and is_valid_password():
            self.data.append(self.user_info)
            with open("users.json", "w") as f:
                json.dump(self.data, f, indent=4)
            console.print("Account created successfully\n", style="bold green")
            self.active_user_account = True

    def login(self, user_name, password):
        self.data = json.load(open("users.json", "r"))
        for item in self.data:
            if user_name == item.get("Username"):
                if item.get("Is_active") == "No":
                    console.print("The user account has been closed by the system administrator."
                                  " You are not allowed to access the account!\n", style="bold red")
                    return False
                if password == item.get("Password"):
                    console.print(f"Welcome {user_name}\n",
                                  style="bold green")
                    self.logged_in = True
                    return True
                else:
                    console.print("You have entered the wrong password!\n", style="bold red")
                    return False

        if not self.logged_in:
            console.print("The username entered is not valid!\n", style="bold red")

    # def get_id_with_username(username):
    #         info_users = json.load(open ("users.json", "r"))
    #         return next((item.get("ID") for item in info_users if username == item.get("Username")), None)


class CreateTask(Model):
    class Priority(Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        CRITICAL = 4

    class Status(Enum):
        BACKLOG = 1
        TODO = 2
        DOING = 3
        DONE = 4
        ARCHIVED = 5

    def __init__(self):
        self.task_unique_identifier = Model()
        self.task_properties = []
        self.title = ""
        self.description = ""
        start_time = datetime.datetime.now()
        self.start_time = start_time.time()
        self.start_date = start_time.date()
        end_datetime = start_time + datetime.timedelta(hours=24)
        self.end_time = end_datetime.time()
        self.end_date = end_datetime.date()
        self.assignees = []
        self.priority = CreateTask.Priority.LOW
        self.status = CreateTask.Status.BACKLOG

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_start_time(self):
        return self.start_time

    def get_start_date(self):
        return self.start_date

    def get_end_time(self):
        return self.end_time

    def get_end_date(self):
        return self.end_date

    def set_priority(self, priority):
        self.priority = priority

    def set_status(self, status):
        self.status = status

    def add_assignees(self, assignee):
        self.assignees.append(assignee)


class CreateProject(Model):
    def __init__(self, title):
        self.id = Model()
        self.data = []
        self.project_details = dict()
        self.title = title
        self.members = []
        self.project_details["Project_ID"] = str(self.id)

    def save_information(self, leader_id):
        self.project_details["Leader_ID"] = leader_id
        self.project_details["Title"] = self.title
        # self.project_details["leader_id"] = self.leader_id
        self.project_details["Members"] = self.members
        self.data = json.load(open("projects.json", "r"))
        self.data.append(self.project_details)
        with open("projects.json", "w") as f:
            json.dump(self.data, f, indent=4)

    def add_members(self, username):
        self.members.append(username)

    def delete(self, username):
        self.members.append(username)


def delete_project(username):
    is_exist_project = False
    console.print("Enter title of your project", style="yellow")
    title = input()
    info_projects = json.load(open("projects.json", "r"))
    info_users = json.load(open("users.json", "r"))

    for item in info_projects:
        if title == item.get("Title"):
            if item.get("Leader_ID") == next(
                    (item.get("ID") for item in info_users if username == item.get("Username")), None):
                is_exist_project = True

    if is_exist_project:
        for i in range(len(info_projects)):
            if info_projects[i].get("Title") == title:
                del info_projects[i]
                with open("projects.json", "w") as f:
                    json.dump(info_projects, f, indent=4)

                console.print("The project was deleted successfully.", style="green")
    else:
        console.print("This project is not valid!\nOr you are not the leader of this project", style="bold red")


def add_user_project(username):
    is_exist_project = False
    console.print("Enter title of your project", style="yellow")
    title = input()
    info_projects = json.load(open("projects.json", "r"))
    info_users = json.load(open("users.json", "r"))

    for item in info_projects:
        if title == item.get("Title"):
            if item.get("Leader_ID") == next(
                    (item.get("ID") for item in info_users if username == item.get("Username")), None):
                is_exist_project = True

    if is_exist_project:
        console.print("Please enter the username you want to add to the project", style="yellow")
        add_user_name = str(input())
        info_users = json.load(open("users.json", "r"))
        if any(add_user_name in item.get("Username") for item in info_users):
            for i in range(len(info_projects)):
                if info_projects[i].get("Title") == title:
                    info_projects[i].get("Members").append(add_user_name)
                    with open("projects.json", "w") as f:
                        json.dump(info_projects, f, indent=4)

                    console.print("User added successfully.", style="green")
        else:
            console.print("Entered username is not valid!", style="bold red")
    else:
        console.print("This project is not valid!\nOr you are not the leader of this project", style="bold red")


def delete_user_project(username):
    is_exist_project = False
    console.print("Enter title of your project", style="yellow")
    title = input()
    info_projects = json.load(open("projects.json", "r"))
    info_users = json.load(open("users.json", "r"))

    for item in info_projects:
        if title == item.get("Title"):
            if item.get("Leader_ID") == next(
                    (item.get("ID") for item in info_users if username == item.get("Username")), None):
                is_exist_project = True

    if is_exist_project:
        console.print("Please enter the username you want to add to the project", style="yellow")
        delete_user_name = str(input())
        info_users = json.load(open("users.json", "r"))
        for i in range(len(info_projects)):
            if info_projects[i].get("Title") == title:
                if delete_user_name in info_projects[i].get("Members"):
                    info_projects[i].get("Members").remove(delete_user_name)
                    with open("projects.json", "w") as f:
                        json.dump(info_projects, f, indent=4)

                    console.print("User added successfully.", style="green")
                else:
                    console.print("Entered username is not valid!", style="bold red")
    else:
        console.print("This project is not valid!\nOr you are not the leader of this project", style="bold red")


def menu():
    while True:
        print("1- Create account\n"
              "2- Login to to your account\n"
              "3- Exit")
        console.print("Enter your select...", style="bold yellow")
        choice = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        user = Account()

        if choice == '1':
            console.print("Enter your username..", style="blue")
            username = input()
            console.print("Enter your password..", style="blue")
            password = input()
            console.print("Enter your email..", style="blue")
            email = input()
            user.register(username, password, email)

        elif choice == '2':
            console.print("Enter your username..", style="blue")
            username = input()
            console.print("Enter your password..", style="blue")
            password = input()
            user.login(username, password)
            while user.logged_in:
                print("1- Create new project\n"
                      "2- Add user in project\n"
                      "3- delete user in project\n"
                      "4- delete project\n"
                      "5- List of projects in which you are the leader\n"
                      "6- List of projects in which you are a regular member\n"
                      "0- Back to main menu")
                console.print("Enter your select...", style="bold yellow")
                choice = input()
                os.system('cls' if os.name == 'nt' else 'clear')

                if choice == '1':
                    console.print("Please choose a title for your project", style="bold yellow")
                    title_project = input()
                    console.print("The construction of the project was completed successfully", style="bold green")
                    project = CreateProject(title_project)

                    info_users = json.load(open("users.json", "r"))
                    leader_id = next((item.get("ID") for item in info_users if username == item.get("Username")), None)
                    project.save_information(leader_id)

                elif choice == '2':
                    add_user_project(username)

                elif choice == '3':
                    delete_user_project(username)

                elif choice == '4':
                    delete_project(username)

                elif choice == '0':
                    break
                else:
                    console.print("Invalid choice.Please try again.", style="bold red")
                    continue

        elif choice == '3':
            break
        else:
            console.print("Invalid choice.Please try again", style="bold red")
            continue


if __name__ == "__main__":
    menu()
