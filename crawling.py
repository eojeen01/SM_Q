from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', db='crdb2', charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)
def store(title, dateDue):
    cur.execute("INSERT INTO totaloffer (title, dateDUe) VALUES (\"%s\", \"%s\")", (title, dateDue))
    cur.execute("DELETE A FROM totaloffer A, totaloffer B WHERE A.id>B.id AND A.title=B.title")
    cur.connection.commit()

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(3)
driver.get('https://www.smu.ac.kr/ko/index.do')
driver.find_element_by_xpath("//*[@id='item_body']/header/div[1]/div[1]/div/div[2]/ul/li[1]/a").click()
driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])
driver.find_element_by_name('user_id').send_keys('202021066')
driver.find_element_by_name('user_password').send_keys('love0812^^')
driver.find_element_by_xpath("//*[@id='firstAuth']/fieldset/ul/li[2]/button").click()
# 로그인 완..
driver.switch_to.window(driver.window_handles[0])
driver.get_window_position(driver.window_handles[0])
driver.implicitly_wait(3)
driver.find_element_by_xpath("//*[@id='item_body']/div/div[4]/div[2]/ul/li[2]/a").click()
# 피어오름으로 이동 완..
driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])
driver.find_element_by_xpath("//*[@id='content01']/div[1]/ul/li[1]/div[2]").click()
# 통합 정보 프로그램 신청 창 완...-

driver.switch_to.window(driver.window_handles[2])
driver.get_window_position(driver.window_handles[2])
# 창 포커스 전환

time.sleep(30)
a=1
for i in range(22):
    # unit 1
    name1 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(5) > div > div').text.strip()
    print(name1)
    date1 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(4) > div > div').text.strip()
    print(date1)
    # category1 = driver.find_element_by_css_selector(
    #     'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(7) > div > div').text.strip()
    # print(category1)
    store(name1, date1)

    # unit 2
    name2 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(5) > div > div').text.strip()
    print(name2)
    date2 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(4) > div > div').text.strip()
    print(date2)
    store(name2, date2)

    # unit 3
    name3 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(5) > div > div').text.strip()
    print(name3)
    date3 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(4) > div > div').text.strip()
    print(date3)
    store(name3, date3)

    # unit 4
    name4 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(4) > div:nth-child(5) > div > div').text.strip()
    print(name4)
    date4 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(4) > div:nth-child(4) > div > div').text.strip()
    print(date4)
    store(name4, date4)

    # unit 5
    name5 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(5) > div:nth-child(5) > div > div').text.strip()
    print(name5)
    date5 = driver.find_element_by_css_selector(
        'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(5) > div:nth-child(4) > div > div').text.strip()
    print(date5)
    store(name5, date5)

    # strip은 양쪽 공백을 지울 수 있으며 특정 문자도 삭제 가능합니다.

    # category2 = driver.find_element_by_css_selector(
    #     'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(7) > div > div').text.strip()
    # category3 = driver.find_element_by_css_selector(
    #     'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(7) > div > div').text.strip()
    # category4 = driver.find_element_by_css_selector(
    #     'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(4) > div:nth-child(7) > div > div').text.strip()
    # category5 = driver.find_element_by_css_selector(
    #     'div > div:nth-child(3) > div > div.cl-grid-detail.cl-grid-detail-band > div > div:nth-child(1) > div > div > div:nth-child(5) > div:nth-child(7) > div > div').text.strip()

    # name = {name1, name2, name3, name4, name5}
    # date = {date1, date2, date3, date4, date5}
    # category = {category1, category2, category3, category4, category5}

    itemlist = driver.find_element_by_css_selector(
        "div > div:nth-child(3) > div > div.cl-grid-detail > div > div:nth-child(2) > div")
    driver.execute_script("arguments[0].scrollBy(0,120)", itemlist)
    time.sleep(1)


print("\n스크롤 완..")