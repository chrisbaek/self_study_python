import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window() #창최대화

url = 'https://boardgamegeek.com/browse/boardgame/page/1'
browser.get(url)


# 데이터 추출
df = pd.read_html(browser.page_source)[0]

print(df)
df.dropna(axis='index', how='all', inplace=True)
df.dropna(axis='columns', how='all', inplace=True)

    # 파일저장
f_name='boardgame.csv'
if os.path.exists(f_name): # 파일이 있다면? 헤더 제외
    df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
        # append Mode, Header/Index 없음, Encoding 한글호환
else : # 파일이 없는 경우라면? 헤더를 포함
    df.to_csv(f_name, encoding='utf-8-sig', index=False)
        # 자동으로 Mode는 쓰기모드이고, Header는 True가 됨
