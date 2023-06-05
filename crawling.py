import os
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

for idx in range(1,40) : # 1이상 40미만 페이지 반복
    # 사전작업 페이지 이동
    browser.get(url+str(idx))

    # 데이터 추출
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df)==0 : # 더이상 가져올 데이터가 없으면
        break

    # 파일저장
    f_name='sise.csv'
    if os.path.exists(f_name): # 파일이 있다면? 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
        # append Mode, Header/Index 없음, Encoding 한글호환
    else : # 파일이 없는 경우라면? 헤더를 포함
        df.to_csv(f_name, encoding='utf-8-sig', index=False)
        # 자동으로 Mode는 쓰기모드이고, Header는 True가 됨
    print(f"{idx}페이지를 완료하였습니다.")

browser.quit()


