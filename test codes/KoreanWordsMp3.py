import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
chrome.get('http://krdic.naver.com/')

wordString = '공장 열 극장 회사 장소 간판 직업 수업  고기  돼지  돼지고기  소  소고기  꽃  값  땅콩  축구 야구 여권  수건 체육  지하철 되다  시작하다  행동하다  소개하다  발견하다 방문하다   잃다  잃어버리다  벗다  웃다 부끄럽다  건강하다    예쁘다  미래    이제  현재   '
# wordString = '차'
wordList = wordString.split()

# loop in wordList
for word in wordList:
    # open the website
    chrome.get('http://krdic.naver.com/')

    # input the work into search box
    searchBox = chrome.find_element_by_id('krdicQuery')
    searchBox.send_keys(word)
    searchBox.send_keys(Keys.ENTER)
    chrome.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a').click()

    try:
        for i in range(1, 5):
            buttonFatherXPath = '//*[@id="content"]/div[2]/ul/li[1]/div/span[' + str(i) + ']'
            print(word + ': ' + str(i))
            # '//*[@id="content"]/div[2]/ul/*' is the root to get the buttons
            #
            # the following path is organized as follows
            # li[\d]: search results are listed by order, the [\d] parameter refers to its index.
            #   if [\d] == 1, it's the first result, and if [\d] == 2, it's the second result.
            # span[\d]: the link is under which <span>
            #   if [\d] == 1, it's under the first <span> tag, and if [\d] == 2, it's under the second <span> tag
            if chrome.find_element_by_xpath(buttonFatherXPath).get_attribute(
                    'class') == 'player_search ajax_pron_sound_0':
                print(word + ' is going to play')
                buttonXPath = buttonFatherXPath + '/span'
                button = chrome.find_element_by_xpath(buttonXPath)
                button.click()

                # get the link and download
                sound_play_link = button.get_attribute('purl')
                urllib.request.urlretrieve(sound_play_link, 'C:/Users/jingy/Downloads/' + word + '.mp3')
                time.sleep(1)
                break
            else:
                continue
    except:
        # the first search result is incorrect, try the second
        try:
            for i in range(1, 5):
                buttonFatherXPath = '//*[@id="content"]/div[2]/ul/li[2]/div/span[' + str(i) + ']'
                print(word + ': ' + str(i))
                # '//*[@id="content"]/div[2]/ul/*' is the root to get the buttons
                #
                # the following path is organized as follows
                # li[\d]: search results are listed by order, the [\d] parameter refers to its index.
                #   if [\d] == 1, it's the first result, and if [\d] == 2, it's the second result.
                # span[\d]: the link is under which <span>
                #   if [\d] == 1, it's under the first <span> tag, and if [\d] == 2, it's under the second <span> tag
                if chrome.find_element_by_xpath(buttonFatherXPath).get_attribute(
                        'class') == 'player_search ajax_pron_sound_0':
                    print(word + ' is going to play')
                    buttonXPath = buttonFatherXPath + '/span'
                    button = chrome.find_element_by_xpath(buttonXPath)
                    button.click()

                    # get the link and download
                    sound_play_link = button.get_attribute('purl')
                    urllib.request.urlretrieve(sound_play_link, 'C:/Users/jingy/Downloads/' + word + '.mp3')
                    time.sleep(1)
                    break
                else:
                    continue
        except:
            # the second search result is incorrect, try the third
            try:
                for i in range(1, 5):
                    buttonFatherXPath = '//*[@id="content"]/div[2]/ul/li[3]/div/span[' + str(i) + ']'
                    print(word + ': ' + str(i))
                    # '//*[@id="content"]/div[2]/ul/*' is the root to get the buttons
                    #
                    # the following path is organized as follows
                    # li[\d]: search results are listed by order, the [\d] parameter refers to its index.
                    #   if [\d] == 1, it's the first result, and if [\d] == 2, it's the second result.
                    # span[\d]: the link is under which <span>
                    #   if [\d] == 1, it's under the first <span> tag, and if [\d] == 2, it's under the second <span> tag
                    if chrome.find_element_by_xpath(buttonFatherXPath).get_attribute(
                            'class') == 'player_search ajax_pron_sound_0':
                        print(word + ' is going to play')
                        buttonXPath = buttonFatherXPath + '/span'
                        button = chrome.find_element_by_xpath(buttonXPath)
                        button.click()

                        # get the link and download
                        sound_play_link = button.get_attribute('purl')
                        urllib.request.urlretrieve(sound_play_link, 'C:/Users/jingy/Downloads/' + word + '.mp3')
                        time.sleep(1)
                        break
                    else:
                        continue
            except:
                print("There isn't a work similar to " + word)
                continue

    print(word + " is processed")
print('word list finished')
chrome.quit()