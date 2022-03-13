from signal import pause
import requests
from bs4 import BeautifulSoup
from model.school import School

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

def get_school_for_city(city_code):
    options = Options()
    options.add_argument("--disable-notifications")
    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get("https://bsb.kh.edu.tw/")
    chrome.set_window_size(1920, 1055)
    chrome.switch_to.frame(0)
    chrome.find_element(By.CSS_SELECTOR, city_code + " > img").click()
    chrome.switch_to.frame(2)
    chrome.find_element(By.CSS_SELECTOR, "tr:nth-child(2) font").click()
    try:
        page = chrome.find_element(By.NAME, "A1")
    except NoSuchElementException:
        print("no page entry")
        return

    while page.is_enabled():
        page.click()
        html_source = chrome.page_source
        #print(html_source)
        soup = BeautifulSoup(html_source, 'html.parser')
        #print(soup.prettify())
        td_list = soup.select("body > table > tbody > tr > td:nth-child(7) > a")
        href_list = [ td['href'] for td in td_list]
        for suffix in href_list:
            url = 'https://bsb.kh.edu.tw/afterschool/register/' + suffix
            school = get_by_url(url)
            yield school
        try:
            page = chrome.find_element(By.LINK_TEXT, "下一頁")
        except NoSuchElementException:
            print("No next page")
            return

def get_by_unit_id(unit):
    return get_by_url("https://bsb.kh.edu.tw/afterschool/register/detail.jsp?unit=" + unit)

def get_by_url(url):
    
    retry = 0
    while True:
        try:
            response = requests.get(url)
            break    # 跳出迴圈
        except ConnectionError:
            print('retry connect to page, times:' + retry)
            retry = retry + 1
        if (retry == 3):
            raise ConnectionError
        else:
            time.sleep(5)
   
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.select("body > table:nth-child(4) > tr:nth-child(2) > td")[0].getText().strip()
    subject = soup.select("body > table:nth-child(4) > tr:nth-child(4) > td")[0].getText().strip()
    address = soup.select("body > table:nth-child(4) > tr:nth-child(5) > td")[0].getText().strip()
    phoneNumber = soup.select("body > table:nth-child(4) > tr:nth-child(7) > td")[0].getText().strip()
    status = soup.select("body > table:nth-child(4) > tr:nth-child(7) > td")[1].getText().strip()
    fax = soup.select("body > table:nth-child(4) > tr:nth-child(11) > td")[0].getText().strip()
    email = soup.select("body > table:nth-child(4) > tr:nth-child(11) > td")[1].getText().strip()
    school = School(name=name, subject=subject, address=address, phoneNumber=phoneNumber, status=status, fax=fax, email=email)
    return school


