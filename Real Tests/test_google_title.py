
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "Google"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com/")
assert browser.title == expected_title

# ctrl + a  will highlight all lines of code
# this is a smoke test (making sure the page is functioning properly)
