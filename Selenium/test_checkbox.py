#To check if the checkbox is selected
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://homepro.herokuapp.com/quote.php")

#Boolean True or False
checkbox_selected = browser.find_element_by_name("subscription").is_selected()


if (checkbox_selected):
    print("Checkbox is selected!!!")
else:
    print("Checbox is not selected!!!")
