from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.mark.smoketest2102
def test_validate_search():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    browser.get("https://www.ebay.com")
    assert browser.title == "Electronics, Cars, Fashion, Collectibles & More | eBay"






