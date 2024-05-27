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

def test_add_member():
    project1 = CreateProject("Trello")
    username1 = "Alireza"
    project1.add_member(username1)
    assert project1.members[-1] == username1

    project2 = CreateProject("IUSTZ")
    username2 = "Mohammad"
    project2.add_member(username2)
    assert project2.members[-1] == username2



