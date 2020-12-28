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

# 出勤ボタンをクリックする
sleep(random.randint(0, 600))
shukkin = driver.find_element_by_name("syussya")
shukkin.click()

# 一応30秒待つ
sleep(30)

# shukkinn.pyに使ったブラウザを閉じる
driver.close()
