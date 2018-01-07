# KoreanWords
The Program is used for collecting audio files from http://krdic.naver.com/, which is the best audio sources I have ever found.
The original way of downloading the mp3s is by checking the url of the audio files and open it in a new tag within Chrome or Firefox.
By using the Selenium, automatically debugger, the human operations will be replaced by the computer, which will accelerate download speed.

In addition, according to my methodology of studying Korean words, I have to write down the Korean words in Korean with its Chinese and English translations.
The teaching materials are from https://www.howtostudykorean.com, which is written in English.
Trusted Chinese translations from https://dict.hjenglish.com/kr/ can be downloaded also by Selenium.

The project will be organized as follows:
Vocabulary Downloader:  used to download given audio files.
Vocabulary Player:      used to play a collection of audio files online.
Vocabulary Translator:  used to find Chinese Translations of the given Korean words.
Vocabulary Helper:      a combination of Vocabulary Downloader, Vocabulary Player, and Vocabulary Translator.(Optional Choice)