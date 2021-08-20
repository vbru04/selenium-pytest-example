import pytest
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize("name", [
    "macbook pro",
    "microsoft surface",
    "raycon earbuds"
])
@pytest.mark.regressiontest
def test_validate_search(browser, name):
    browser.get("https://www.ebay.com")
    assert browser.title == "Electronics, Cars, Fashion, Collectibles & More | eBay"
    browser.find_element_by_id("twotabsearchtextbox").send_keys(name + Keys.ENTER)
