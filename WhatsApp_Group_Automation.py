from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get('https://web.whatsapp.com/')

sleep(10)

try:
    menu_btn = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                   "//*[@id='app']/div/div[2]/div[3]/header/div[2]/div/span/div[5]/div/span")
                                   )
    )
    sleep(5)
    menu_btn.click()
    sleep(1)

    new_group_btn = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                    "//*[@id='app']/div/div[2]/div[3]/header/div[2]/div/span/div[5]/span/div/ul/li[1]/div")
                                   )
    )

    sleep(1)
    new_group_btn.click()

    sleep(1)


    input_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/div[2]/input"))
    )
    input_box.click()


    sleep(1)

    input_box.send_keys("Vansh")

    sleep(2)

    user_name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div"))
    )
    sleep(2)

    user_name.click()

    sleep(2)

    arrow_btn = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div/span/div/span"))
    )

    sleep(2)

    arrow_btn.click()

    sleep(2)

    group_name_inp_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/p"
                                        )
                                       )
    )

    group_name_inp_box.click()
    sleep(1)
    group_name_inp_box.send_keys("Python Whatsapp Automation by Dev")

    sleep(2)

    done_btn = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div/span/div/div/span"))
    )

    sleep(2)

    done_btn.click()
    sleep(7)
    driver.quit()
    print("Group has been created successfully !!! ")

except Exception as E:
    print(E)