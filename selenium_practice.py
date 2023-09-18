from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Firefox()
url = "http://localhost/xyz/wp-login.php"

driver.get(url)
password = "1821093042@"
username = "admin"

driver.find_element("id", "user_login").send_keys(username)
print("one")
driver.find_element("id", "user_pass").send_keys(password)
print("two")
driver.find_element("name", "wp-submit").click()
print("three")



plugin_url = "http://localhost/xyz/wp-admin/plugins.php"
wp_dark_url = "http://localhost/xyz/wp-admin/admin.php?page=wp-dark-mode-settings"
driver.get(plugin_url)
search_bar = driver.find_element("name","s")
print("searching")
search_bar.clear()
search_bar.send_keys("wp dark mode")

data = driver.find_element('id','deactivate-wp-dark-mode')
# print(data)

if data.text == "Deactivate":
    # print(" wp-dark mode is already activated")
    driver.get(wp_dark_url)
    dark = driver.find_elements('id','wppool-wp_dark_mode_general[enable_backend]')[0]
    if dark.is_selected() == False:
        dark.click()
        print(dark.is_selected())

else:
    print("will activate here")
