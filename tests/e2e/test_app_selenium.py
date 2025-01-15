from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Login"


def test_app(client):
    response = client.get("/app")
    assert response.status_code == 200
    assert response.data == b"App"


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")

    try:
        test_login(driver)
        test_app(driver)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
