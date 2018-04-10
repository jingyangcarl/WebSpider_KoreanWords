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
# web page url
url = "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-1/"
# downloadPath is used for indicating the path to store files
dirPath = 'C:/Users/jingy/Downloads/HowToStudyKorean/'
# fileFormat is used for indicating the file storage format
fileFormat = ".mp3"

# --------------------------------CODE---------------------------------------
# unit number
unit = re.search('unit\d*/', url).group(0)
dirPath = dirPath + unit
# lesson number
lesson = re.search('lesson-\d*/', url).group(0)
# dirpath
dirPath = dirPath + lesson
if not os.path.exists(dirPath):
    os.makedirs(dirPath)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
request = urllib.request.Request(url, headers=headers)
HTMLRetryTime = 0
audioNum = 0

while 1:
    try:
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
                downloadRetryTime = 0

                while not os.path.isfile(downloadPath):
                    try:
                        audioRequest = urllib.request.Request(audioLink, headers=headers)
                        requestHTML = urllib.request.urlopen(audioRequest).read()
                        audio = open(downloadPath, 'wb')
                        audio.write(requestHTML)
                        audio.close()
                        audioNum = audioNum + 1
                        print(audioName + " downloaded")
                    except:
                        downloadRetryTime = downloadRetryTime + 1
                        print(audioName + " download retry: " + str(downloadRetryTime))
        print('all finished')
        print('Audios: ' + str(audioNum))
        os._exit(0)
    except:
        HTMLRetryTime = HTMLRetryTime + 1
        print("html retry: " + str(HTMLRetryTime))