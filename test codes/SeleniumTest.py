import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://krdic.naver.com/")

#time.sleep(2)

search_box = driver.find_element_by_id('krdicQuery')
search_box.send_keys('중국')
search_box.send_keys(Keys.ENTER)

sound_play_button_father_path = '//*[@id="content"]/div[2]/ul/li[1]/div/span[2]'
# '//*[@id="content"]/div[2]/ul/*' is the root to get the bottons
#
# the following path is organized as follows
# li[\d]: search results are listed by order, the [\d] parameter refers to its index.
#   if [\d] == 1, it's the first result, and if [\d] == 2, it's the second result.
# span[\d]: the link is under which <span>
#   if [\d] == 1, it's under the first <span> tag, and if [\d] == 2, it's under the second <span> tag

# if the class name of xpath is 'player_search ajax_pron_sound_0', the son node is the mp3 botton
sound_play_button_father = driver.find_element_by_xpath(sound_play_button_father_path)
button_father_class = sound_play_button_father.get_attribute('class')
if button_father_class == 'player_search ajax_pron_sound_0':
    sound_play_button_path = sound_play_button_father_path + '/span'
    sound_play_button = driver.find_element_by_xpath(sound_play_button_path)

    # play the sound
    #sound_play_button.click()

    # get the link
    sound_play_link = sound_play_button.get_attribute('purl')

    # download the link
    #driver.get(sound_play_link)
    #mp3_source = driver.page_source
    urllib.request.urlretrieve(sound_play_link, "D:/text.mp3")

    # open a new tab
    #driver.execute_script('''window.open("about:blank", "_blank");''')
else:
    # change the path from '//*[@id="content"]/div[2]/ul/li[1]/div/span[2]' to '//*[@id="content"]/div[2]/ul/li[1]/div/span[3]'
    sound_play_button_father_path_list = list(sound_play_button_father_path)
    sound_play_button_father_path_list[44] = '3'
    sound_play_button_father_path = ''.join(sound_play_button_father_path_list)

    # if the class name of xpath is 'player_search ajax_pron_sound_0', the son node is the mp3 botton
    sound_play_button_father = driver.find_element_by_xpath(sound_play_button_father_path)
    button_father_class = sound_play_button_father.get_attribute('class')
    if button_father_class == 'player_search ajax_pron_sound_0':
        sound_play_button_path = sound_play_button_father_path + '/span'
        sound_play_button = driver.find_element_by_xpath(sound_play_button_path)
        sound_play_button.click()
    else:
        # change the path from '//*[@id="content"]/div[2]/ul/li[1]/div/span[3]' to '//*[@id="content"]/div[2]/ul/li[1]/div/span[4]'
        sound_play_button_father_path_list = list(sound_play_button_father_path)
        sound_play_button_father_path_list[44] = '4'
        sound_play_button_father_path = ''.join(sound_play_button_father_path_list)

        # if the class name of xpath is 'player_search ajax_pron_sound_0', the son node is the mp3 botton
        sound_play_button_father = driver.find_element_by_xpath(sound_play_button_father_path)
        button_father_class = sound_play_button_father.get_attribute('class')
        if button_father_class == 'player_search ajax_pron_sound_0':
            sound_play_button_path = sound_play_button_father_path + '/span'
            sound_play_button = driver.find_element_by_xpath(sound_play_button_path)
            sound_play_button.click()
        else:
            # change the path from '//*[@id="content"]/div[2]/ul/li[1]/div/span[4]' to '//*[@id="content"]/div[2]/ul/li[1]/div/span[1]'
            print("unknown")

time.sleep(2)
driver.quit()