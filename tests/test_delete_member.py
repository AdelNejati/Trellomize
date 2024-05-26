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

def test_delete_member():
    project1 = CreateProject("Trello")
    username1 = "Amin"
    project1.add_member(username1)
    project1.delete_member(username1)
    assert username1 not in project1.members

    project2 = CreateProject("IUSTZ")
    username2 = "Abbas"
    project2.add_member(username2)
    project2.delete_member(username2)
    assert username2 not in project2.members
