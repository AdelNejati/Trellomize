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


def test_is_valid_gmail():
    account = Account()
    email1 = "adel@yahoo.com"
    email2 = "ali@gmail.com"
    email3 = "amin@iust.ir"
    assert account.register()