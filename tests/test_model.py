import pytest
import uuid 
from main import Model


def test_model():
    model = Model()
    # model.add_users()
    assert model.id is not None
    # assert model.users[-1] is "Adel"
    # model.add_users("Ali")

    
    
