import time
from selenium import webdriver

# -------------------------------FUNCTION------------------------------------
# The code is used for translating Korean words into Chinese as a guider and help with the correctness of spelling.
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
wordString = '경제 경제적 역사 역사적 과학 과학적 충동 충동적 문화 문화적 민주 민주적 개인 개인적 자연 자연스럽다 실망' \
             ' 실망스럽다 사랑 사랑스럽다 만족 만족스럽다 관계 스트레스 연필 색깔 그 그녀 결과 꿈 세상 세계 회화 문자 ' \
             '가슴 제목 풀다 꿈꾸다 태어나다 다니다 믿다 가깝다 힘들다 순수하다 조금 근처 나중에 최근에 그러나 '
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
        time.sleep(timeStep)
    except:
        continue

chrome.quit()
