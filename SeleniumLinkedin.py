from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com")
sleep(1)
driver.execute_script("document.body.style.zoom='1.5'")
sleep(1)
input = driver.find_element(By.NAME, "q")
input.send_keys("Atacan GÜZELKAYA")
sleep(1)
input.send_keys(Keys.ENTER)
sleep(1)
driver.execute_script("document.body.style.zoom='1.25'")
sleep(3)
linked = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a").click()
sleep(2)
driver.execute_script("document.body.style.zoom='1.25'")
sleep(1)
driver.execute_script("document.body.style.opacity = '0.5';")
sleep(2)
driver.execute_script("alert('Suanda Atacan GUZELKAYA adli kisinin profilini inceliyorsunuz. Profili inceledikten sonra ona bir is firsati vermeye ne dersiniz?');")
sleep(8)
alert = driver.switch_to.alert
alert.dismiss()
driver.execute_script("document.body.style.opacity = '1';")
sleep(30)
driver.quit()