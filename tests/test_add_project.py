from rich import console, table
from rich.table import Table
import os
import json
import re
import uuid
import datetime
from enum import Enum
import bcrypt
import pytest
from main import Account

def test_add_project():
    account = Account()
    project1 = {
        "Project_ID": "<__main__.Model object at 0x00000187EDE698E0>",
        "Leader_ID": "<__main__.Model object at 0x00000187EC33E2D0>",
        "Title": "",
        "Members": [],
        "Tasks": [
            "t1",
            "t2"
        ],
        "Tasks Data": [
            {
                "Task ID": "<__main__.Model object at 0x00000187EDE4AC60>",
                "Title": "t1",
                "Description": "vfl",
                "Start Time": "02:40:02.454959",
                "Start Date": "2024-05-26",
                "End Time": "02:40:02.454959",
                "End Date": "2024-05-27",
                "Assignees": [],
                "Priority": "Priority.LOW",
                "Status": "Status.BACKLOG",
                "Comments": []
            },
            {
                "Task ID": "<__main__.Model object at 0x00000187EDE4B3B0>",
                "Title": "t2",
                "Description": "vdiopfd",
                "Start Time": "02:41:06.169465",
                "Start Date": "2024-05-26",
                "End Time": "02:41:06.169465",
                "End Date": "2024-05-27",
                "Assignees": [],
                "Priority": "Priority.LOW",
                "Status": "Status.BACKLOG",
                "Comments": []
            }
        ]
    }
    project2 = {
        "Project_ID": "<__main__.Model object at 0x0000024F979DC770>",
        "Leader_ID": "<__main__.Model object at 0x0000024F95F1D760>",
        "Title": "",
        "Members": [
            "Mohammad"
        ],
        "Tasks": [
            "t2"
        ],
        "Tasks Data": [
            {
                "Task ID": "<__main__.Model object at 0x0000024F979CAF60>",
                "Title": "t2",
                "Description": "nsodincosid",
                "Start Time": "23:45:56.815713",
                "Start Date": "2024-05-26",
                "End Time": "23:45:56.815713",
                "End Date": "2024-05-27",
                "Assignees": [],
                "Priority": "Priority.LOW",
                "Status": "Status.BACKLOG",
                "Comments": []
            }
        ]
    }
    account.add_project(project1)
    assert account.projects[-1] == project1
    account.add_project(project2)
    assert account.projects[-1] == project2



