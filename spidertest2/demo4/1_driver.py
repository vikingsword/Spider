
from selenium import webdriver

if __name__ == "__main__":
    browser = webdriver.Chrome('D:\chrome\driver\chromedriver.exe')
    browser.get('https://www.baidu.com/')