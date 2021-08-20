from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Amazon"
search_page_title = "Amazon - MacBook pro"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.amazon.com/")
assert browser.title == expected_title

browser.find_element_by_name("field keywords").send_keys("MacBook Pro" + Keys.ENTER)
assert browser.title == search_page_title








