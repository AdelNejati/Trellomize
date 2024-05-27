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

def test_add_task():
    project1 = CreateProject("Trello")
    task1 = "t1"
    project1.add_task(task1)
    assert project1.tasks[-1] == task1

    project2 = CreateProject("IUSTZ")
    task2 = "t2"
    project2.add_task(task2)
    assert project2.tasks[-1] == task2



