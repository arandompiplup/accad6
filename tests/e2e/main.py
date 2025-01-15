from selenium import webdriver
from selenium.webdriver.common.by import By


def test_app(url):
    print("Testing app")
    driver = webdriver.Firefox()

    try:
        driver.get(url)
        assert driver.title == "Login"

        driver.find_element(By.Name("username")).send_keys("test")
        driver.find_element(By.Type("submit")).click()

        assert driver.title == "App"
        assert driver.find_element(By.TagName("h2")).text == "User: test"

        driver.find_element(By.Name("clicker")).click()
        assert driver.find_element(By.TagName("p")).text == "Bananas: 1"

        driver.find_element(By.Name("deleter")).click()
        assert driver.title == "Login"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_app("http://localhost:8080")
