from selenium import webdriver
from time import sleep
import var as file
import random
driver_path = file.driver_path

account_user = file.account_user
account_pass = file.account_pass
page = file.page

driver = webdriver.Chrome(driver_path)
driver.get(page)

# ユーザ名・パスワードを入力する場所を探す
user = driver.find_element_by_name("user_id")
pass_word = driver.find_element_by_name("password")

# ユーザ名・パスワードを入力する
user.send_keys(account_user)
pass_word.send_keys(account_pass)

# 退勤ボタンを押す
sleep(random.randint(0, 600))
taisha = driver.find_element_by_name("taisya")
taisha.click()

# 一応30秒待機する
sleep(30)

# 打刻に使ったブラウザを閉じる
driver.close()