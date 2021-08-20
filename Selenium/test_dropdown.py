from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://the-internet.herokuapp.com/")
browser.find_element_by_link_text("Dropdown").click()
