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
from main import hash_password


def test_register1():
    account1 = Account()
    account1.register("Adel", "65616&&%$#vjbsfh", "adel@gmail.com")
    assert account1.user_info["Username"] == "Adel"
    assert account1.user_info["Email"] == "adel@gmail.com"
    assert account1.user_info["Is_active"] is not None
    assert account1.user_info["Regular_member"] is not None
    assert account1.user_info["Leader_member"] is not None
    assert account1.user_data is not None


def test_register2():
    account2 = Account()
    account2.register("Ali", "@bCdbs^%221!@#$", "ali@yahoo.com")
    assert account2.user_info["Username"] == "Ali"
    assert account2.user_info["Email"] == "ali@yahoo.com"
    assert account2.user_info["Is_active"] is not None
    assert account2.user_info["Regular_member"] is not None
    assert account2.user_info["Leader_member"] is not None
    assert account2.user_data is not None



# if __name__ == "__main__":
#     test_register1()
#     test_register2()
#     print("py ./manager.py purge-data")

