from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')
navegador.get('https://portal.unisal.br:8081/web/app/edu/PortalEducacional/#/')
time.sleep(3)
navegador.find_element(By.XPATH,'/html/body/div[2]/div[3]/form/div[1]/input').send_keys("LOGIN")
navegador.find_element(By.XPATH,'//*[@id="Pass"]').send_keys("SENHA")
navegador.find_element(By.XPATH ,'/html/body/div[2]/div[3]/form/div[4]/input').click()
time.sleep(10)
navegador.find_element(By.XPATH , '/html/body/div[2]/div[2]/div/div/div[1]/div[1]/ul/li[11]').click()