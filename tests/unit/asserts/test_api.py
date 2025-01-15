import importlib
from pytest import fixture

import pynamodb

api = importlib.import_module("src.api")

@fixture
def user():
    return api.createBanana("test")

def test_createBanana(user):
    assert user.username == "test" and user.banana == 0


def test_readBananaFull(user):
    username = user.username
    banana = user.banana
    assert api.readBananaFull(username).username == username and api.readBananaFull(username).banana == banana


def test_readBananaNum(user):
    username = user.username
    banana = user.banana
    assert api.readBananaNum(username) == banana


def test_addBanana(user):
    username = user.username
    banana = user.banana
    api.addBanana(username, banana + 1)
    assert api.readBananaNum(username) == banana + 1


def test_deleteUser(user):
    username = user.username
    api.deleteUser(username)
    assert api.Banana.username
