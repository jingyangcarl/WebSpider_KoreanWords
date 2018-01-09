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
wordString = '일월 이월 삼월 사월 오월 유월 칠월 팔월 구월 시월 십일월 십이월 기회 계획 회사원 요리사 운전사 달리다 ' \
             '요리하다 운전하다 죽다 두렵다 이상하다 동안 달 개월 날 하루 이틀 사흘 지난 주 지난 달 이번 주 이번 달 ' \
             '다음 주 다음 달 작년 올해 내년 평생 보통  '
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
