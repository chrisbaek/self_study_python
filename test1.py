import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window() #창최대화

url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)


# 조회 항목 초기화
checkboxes = browser.find_elements(By.NAME, 'fieldIds')

for checkbox in checkboxes :
    if checkbox.is_selected():  #체크된 상태라면?
        checkbox.click()   #체크를 해제하라
# 조회 항목 설정

items_to_select = ['영업이익', '자산총계', '매출액']

for checkbox in checkboxes :
    parent = checkbox.find_element(By.XPATH, '..')
    label = parent.find_element(By.TAG_NAME, 'label')
    # print(label.text) # 이름확인
    if label.text in items_to_select :
        checkbox.click()

# 적용하기 버튼 클릭
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

# 데이터 추출
df = pd.read_html(browser.page_source)[1]
df.dropna(axis='index', how='all', inplace=True)
df.dropna(axis='columns', how='all', inplace=True)


