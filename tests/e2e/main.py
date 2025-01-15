from selenium import webdriver
from selenium.webdriver.common.by import By


def test_app(url):
    print("Testing app")
    driver = webdriver.Firefox()

    try:
        driver.get(url)
        assert driver.title == "Login"

        driver.find_element(By.NAME, "username").send_keys("test")
        driver.find_element(By.NAME, "login").click()

        assert driver.title == "App"
        assert driver.find_element(By.TAGNAME, "h2").text == "User: test"

        driver.find_element(By.NAME, "clicker").click()
        assert driver.find_element(By.TAGNAME, "p").text == "Bananas: 1"

        driver.find_element(By.NAME, "deleter").click()
        assert driver.title == "Login"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_app("http://localhost:8080")
