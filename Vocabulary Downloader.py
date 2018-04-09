import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# -------------------------------FUNCTION------------------------------------
# The code is used for downloading audio files of given Korean words.
# Audio files are from http://krdic.naver.com/ which is created by Korean.
# By setting the environment and parameters, the code will automatically operate Chrome for given words,
# Files will be downloaded to the user indicated path.
# If there is already a file with the same name, the new one will replace the old one.

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
chrome.get('http://krdic.naver.com/')

# -----------------------------PARAMETER-------------------------------------
# wordString is used for storing the word list.
wordString =  '경제 경제적 역사 역사적 과학 과학적 충동 충동적 문화 문화적 민주 민주적 개인 개인적 자연 자연스럽다 실망' \
             ' 실망스럽다 사랑 사랑스럽다 만족 만족스럽다 관계 스트레스 연필 색깔 그 그녀 결과 꿈 세상 세계 회화 문자 ' \
             '가슴 제목 풀다 꿈꾸다 태어나다 다니다 믿다 가깝다 힘들다 순수하다 조금 근처 나중에 최근에 그러나 '
# downloadPath is used for indicating the path to store files
downloadPath = 'C:/Users/jingy/Downloads/'
# fileFormat is used for indicating the file storage format
fileFormat = ".mp3"
# timeStep is used for control the time break between each word.
timeStep = 5

# --------------------------------CODE---------------------------------------
wordList = wordString.split()

# loop in wordList
for word in wordList:
    # open the website
    chrome.get('http://krdic.naver.com/')

    # input the work into search box
    searchBox = chrome.find_element_by_id('krdicQuery')
    searchBox.send_keys(word)
    searchBox.send_keys(Keys.ENTER)

    # switch to 단어
    chrome.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a').click()

    try:
        # try the first search result
        for i in range(1, 5):
            buttonFatherXPath = '//*[@id="content"]/div[2]/ul/li[1]/div/span[' + str(i) + ']'
            print(word + ': ' + str(i))
            # '//*[@id="content"]/div[2]/ul/*' is the root to get the buttons
            #
            # the following path is organized as follows
            # li[\d]: search results are listed by order, the [\d] refers to its index.
            #   if [\d] == 1, it's the first result.
            # span[\d]: the link is under which <span>
            #   if [\d] == 1, it's under the first <span> tag.
            if chrome.find_element_by_xpath(buttonFatherXPath).get_attribute(
                    'class') == 'player_search ajax_pron_sound_0':
                print(word + ' is going to download')
                buttonXPath = buttonFatherXPath + '/span'
                button = chrome.find_element_by_xpath(buttonXPath)

                # play the mp3
                button.click()

                # get the link and download
                fileURL = button.get_attribute('purl')
                urllib.request.urlretrieve(fileURL, downloadPath + word + fileFormat)
                break
            else:
                continue
    except:
        # the first search result is incorrect, try the second
        try:
            # try the second search result
            for i in range(1, 5):
                buttonFatherXPath = '//*[@id="content"]/div[2]/ul/li[2]/div/span[' + str(i) + ']'
                print(word + ': ' + str(i))
                # '//*[@id="content"]/div[2]/ul/*' is the root to get the buttons
                #
                # the following path is organized as follows
                # li[\d]: search results are listed by order, the [\d] refers to its index.
                #   if [\d] == 1, it's the first result.
                # span[\d]: the link is under which <span>
                #   if [\d] == 1, it's under the first <span> tag.
                if chrome.find_element_by_xpath(buttonFatherXPath).get_attribute(
                        'class') == 'player_search ajax_pron_sound_0':
                    print(word + ' is going to download')
                    buttonXPath = buttonFatherXPath + '/span'
                    button = chrome.find_element_by_xpath(buttonXPath)

                    # play the mp3
                    button.click()

                    # get the link and download
                    fileURL = button.get_attribute('purl')
                    urllib.request.urlretrieve(fileURL, downloadPath + word + fileFormat)
                    break
                else:
                    continue
        except:
            # the second search result is incorrect, try the third
            try:
                # try the third search result
                for i in range(1, 5):
                    buttonFatherXPath = '//*[@id="content"]/div[2]/ul/li[3]/div/span[' + str(i) + ']'
                    print(word + ': ' + str(i))
                    # '//*[@id="content"]/div[2]/ul/*' is the root to get the buttons
                    #
                    # the following path is organized as follows
                    # li[\d]: search results are listed by order, the [\d] refers to its index.
                    #   if [\d] == 1, it's the first result.
                    # span[\d]: the link is under which <span>
                    #   if [\d] == 1, it's under the first <span> tag.
                    if chrome.find_element_by_xpath(buttonFatherXPath).get_attribute(
                            'class') == 'player_search ajax_pron_sound_0':
                        print(word + ' is going to download')
                        buttonXPath = buttonFatherXPath + '/span'
                        button = chrome.find_element_by_xpath(buttonXPath)

                        # play the mp3
                        button.click()

                        # get the link and download
                        fileURL = button.get_attribute('purl')
                        urllib.request.urlretrieve(fileURL, downloadPath + word + fileFormat)
                        break
                    else:
                        continue
            except:
                print("There isn't a word similar to " + word)
                continue

    print(word + " is processed")
    time.sleep(timeStep)
print('word list finished')

chrome.quit()
