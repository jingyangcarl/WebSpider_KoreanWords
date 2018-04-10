import urllib.request
import re
import os.path

# -------------------------------FUNCTION------------------------------------
# The code is used for downloading audio files of given Webpage
# Audio files are from https://www.howtostudykorean.com/ which is created by Korean.
# By setting the environment and parameters, the code will automatically download all the audio files on a web pages,
# Files will be downloaded to the user indicated path.
# If there is already a file with the same name, the new one will replace the old one.

# -----------------------------ENVIRONMENT-----------------------------------
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.2

# -----------------------------PARAMETER-------------------------------------
# downloadPath is used for indicating the path to store files
dir = 'C:/Users/jingy/Downloads/HowToStudyKorean/'
# fileFormat is used for indicating the file storage format
fileFormat = ".mp3"

# --------------------------------CODE---------------------------------------
# web page url
url = 'https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-1/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/24.0'}
HTMLRetryTime = 0
lesson = 1

while lesson:

    try:
        # unit number
        #unit = re.search('unit\d*/', url).group(0)
        #dirPath = dir + unit
        unit = int(lesson/25) + 1
        dirPath = dir + 'unit' + str(unit) + '/lesson-' + str(lesson) + '/'
        # lesson number
        #lesson = re.search('lesson-\d*/', url).group(0)
        #dirPath = dirPath + lesson

        # create path
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        request = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(request).readlines()

        for line in html:
            # bytes to str
            line = bytes.decode(line)
            # remove '\n'
            line = line.strip('\n')
            audioLine = re.search('<a href=".*?\.mp3">.*?</a>', line)
            if audioLine:
                audioLine = audioLine.group(0)

                # get audio link
                audioLink = re.search('http.*\.mp3', audioLine)
                audioLink = audioLink.group(0)
                print("audioLink: " + audioLink)

                # get audio name
                audioName = re.search('>.*<', audioLine)
                audioName = audioName.group(0).lstrip('>').rstrip('<')
                audioName = re.sub('<.*?>', '', audioName)
                audioName = re.sub('[?!/|]', '', audioName)
                # if there is an illegal symbols, add it into the pattern
                print("audioName: " + audioName)

                # prepare for downloading
                downloadPath = dirPath + audioName + fileFormat
                print(downloadPath)

                while not os.path.isfile(downloadPath):
                    try:
                        audioRequest = urllib.request.Request(audioLink, headers=headers)
                        requestHTML = urllib.request.urlopen(audioRequest).read()
                        audio = open(downloadPath, 'wb')
                        audio.write(requestHTML)
                        audio.close()
                        print(audioName + " downloaded")
                    except urllib.error.URLError:
                        print(audioName + " download retry")

            # find the next link
            #nextLinkLine_1 = re.search('<a href=".*to the next lesson!</a>', line)
            nextLinkLine_2 = re.search('Lesson \d+', line)

            #if nextLinkLine_1 and nextLinkLine_2:
            #    url = re.search('http.*"', nextLinkLine_1.group(0)).group(0).rstrip('"')
            #elif nextLinkLine_1:
            #    url = re.search('http.*"', nextLinkLine_1.group(0)).group(0).rstrip('"')
            if nextLinkLine_2:
                # check the lesson number
                nextLinkLine_2 = re.search('\d+$', nextLinkLine_2.group(0)).group(0)
                # check if the unit number is 0
                check = re.search('unit0', line)

                if int(nextLinkLine_2) == (lesson+1) and not check:
                    url = re.search('http.*?"', line).group(0).rstrip('"')

        print('lesson ' + str(lesson) + ' finished')
        print('next url: ' + url)
        lesson = lesson + 1

    except urllib.error.URLError:
        print("html retry")