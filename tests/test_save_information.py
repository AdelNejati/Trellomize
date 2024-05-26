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
from main import CreateProject


def test_save_information():
    project1 = CreateProject("Trello")
    leader_id = str(uuid.uuid4())
    project1.save_information(leader_id)
    assert project1.project_details["Leader_ID"] == leader_id
    assert project1.project_details["Title"] == "Trello"
    assert project1.project_details["Members"] == project1.members
    assert project1.project_details["Tasks"] == [task.title for task in project1.tasks]
    assert project1.project_details["Tasks Data"] == [
            {"Task ID": task.task_unique_identifier,
             "Title": task.title,
             "Description": task.description,
             "Start Time": str(task.start_time),
             "Start Date": str(task.start_date),
             "End Time": str(task.end_time),
             "End Date": str(task.end_date),
             "Assignees": task.assignees,
             "Priority": str(task.priority)[9:],
             "Status": str(task.status)[7:],
             "Priority": str(task.priority),
             "Status": str(task.status),
             "Comments": task.comments, } for task in project1.tasks
        ]

    project2 = CreateProject("IUSTZ")
    leader_id = str(uuid.uuid4())
    project2.save_information(leader_id)
    assert project2.project_details["Leader_ID"] == leader_id
    assert project2.project_details["Title"] == "IUSTZ"
    assert project2.project_details["Members"] == project1.members
    assert project2.project_details["Tasks"] == [task.title for task in project1.tasks]
    assert project2.project_details["Tasks Data"] == [
            {"Task ID": task.task_unique_identifier,
             "Title": task.title,
             "Description": task.description,
             "Start Time": str(task.start_time),
             "Start Date": str(task.start_date),
             "End Time": str(task.end_time),
             "End Date": str(task.end_date),
             "Assignees": task.assignees,
             "Priority": str(task.priority)[9:],
             "Status": str(task.status)[7:],
             "Priority": str(task.priority),
             "Status": str(task.status),
             "Comments": task.comments, } for task in project1.tasks
        ]
