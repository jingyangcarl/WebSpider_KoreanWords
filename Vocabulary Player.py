import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# -------------------------------FUNCTION------------------------------------
# The code is used for play audio files of given Korean words.
# The audio files are from http://krdic.naver.com/ which is created by Korean.
# By setting the environment and parameters, the code will automatically operate Chrome for given words,

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
wordString = ' 하나 둘 셋 넷 다섯 여섯 일곱 여덟 아홉 열 스물 서른 마흔 쉰 일 이 삼 사 오 육 칠 팔 구 십 백 천 만 영 공 ' \
             '처음 마지막 번째 첫 번째 두 번째 개 번 명 대 잔 시 분 초 살 '
# timeStep is used for control the time break between each word.
timeStep = 3.5

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
                print(word + ' is going to play')
                buttonXPath = buttonFatherXPath + '/span'
                button = chrome.find_element_by_xpath(buttonXPath)

                # play the mp3
                button.click()
                time.sleep(timeStep)
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
                    print(word + ' is going to play')
                    buttonXPath = buttonFatherXPath + '/span'
                    button = chrome.find_element_by_xpath(buttonXPath)

                    # play the mp3
                    button.click()
                    time.sleep(timeStep)
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
                        print(word + ' is going to play')
                        buttonXPath = buttonFatherXPath + '/span'
                        button = chrome.find_element_by_xpath(buttonXPath)

                        # play the mp3
                        button.click()
                        time.sleep(timeStep)
                        break
                    else:
                        continue
            except:
                print("There isn't a word similar to " + word)
                continue

    print(word + " is processed")
print('word list finished')

chrome.quit()
