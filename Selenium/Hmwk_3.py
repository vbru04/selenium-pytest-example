from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Amazon"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.amazon.com/")
assert browser.title == expected_title
assert browser.title
browser.find_element_by_link_text("Kindle Books").click()



