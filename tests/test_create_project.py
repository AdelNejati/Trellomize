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


def test_CreateProject():
    project1 = CreateProject("Trello")
    assert project1.title == "Trello"
    project2 = CreateProject("IUSTZ")
    assert project2.title == "IUSTZ"

