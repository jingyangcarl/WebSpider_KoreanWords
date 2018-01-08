import time
from selenium import webdriver

# -------------------------------FUNCTION------------------------------------
# The code is used for translate Korean words into Chinese as a guider and help with the correctness of spelling.
# Chinese translations are from https://dict.hjenglish.com/kr/, which is a dictionary for different languages.
# By setting the environment and parameters, the code will automatically operate Chrome for given words.

# -----------------------------ENVIRONMENT-----------------------------------
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.2
# Selenium 2
# ChromeDriver

# Selenium: https://selenium-python.readthedocs.io/index.html
# ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/getting-started

# ---------------------------INITIALIZATION----------------------------------
chrome = webdriver.Chrome()
chrome.get('https://dict.hjenglish.com/kr/')

# -----------------------------PARAMETER-------------------------------------
# wordString is used for storing the word list.
wordString = '하나 둘 셋 넷 다섯 여섯 일곱 여덟 아홉 열 스물 서른 마흔 쉰 일 이 삼 사 오 육 칠 팔 구 십 백 천 만 영 공 ' \
             '처음 마지막 번째 첫 번째 두 번째 개 번 명 대 잔 시 분 초 살 '
# timeStep is used for control the time break between each word.
timeStep = 5

# --------------------------------CODE---------------------------------------
wordList = wordString.split()

# loop in wordList
for word in wordList:
    # open the website
    try:
        chrome.get('https://dict.hjenglish.com/kr/' + str(word))
        print(word + " is processed")
        time.sleep(5)
    except:
        continue

chrome.quit()
