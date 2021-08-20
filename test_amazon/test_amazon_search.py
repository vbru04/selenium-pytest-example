from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    yield browser


@pytest.mark.regressiontest
def test_validate_title(browser):
    browser.get("https://www.amazon.com")
    assert browser.title == "Amazon.com. Spend less. Smile more."


@pytest.mark.regressiontest
def test_validate_search(browser):
    browser.get("https://www.amazon.com")
    assert browser.title == "Amazon.com. Spend less. Smile more."
    browser.find_element_by_id("twotabsearchtextbox").send_keys("macbook pro" + Keys.ENTER)
