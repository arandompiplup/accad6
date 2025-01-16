from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


def test_app(url):
    print("Testing app")
    driver = webdriver.Firefox()

    try:
        use_app(driver, url)
    finally:
        sleep(2)
        driver.quit()


def use_app(driver, url):
    driver.get(url)
    assert driver.title == "Login"
    sleep(2)

    driver.find_element(By.NAME, "username").send_keys("test")
    sleep(2)
    driver.find_element(By.NAME, "login").click()

    assert driver.title == "App"
    assert driver.find_element(By.TAG_NAME, "h2").text == "test"

    sleep(2)

    driver.find_element(By.NAME, "clicker").click()
    assert (
        driver.find_element(By.NAME, "local-bananas").text == "Local Bananas: 1 (+1)"
        and driver.find_element(By.NAME, "cloud-bananas").text == "Cloud Bananas: 0"
    )

    sleep(2)

    driver.find_element(By.NAME, "deleter").click()
    assert driver.title == "Login"


if __name__ == "__main__":
    test_app("http://localhost:8080")
