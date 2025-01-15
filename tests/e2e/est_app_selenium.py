from pytest import fixture

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_app(client):
    assert True