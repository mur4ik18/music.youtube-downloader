from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import youtube_dl

# add webdriver
driver = webdriver.Chrome('chromedriver')
# open stackoverflow
driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
# Musick links list
musicList=[]
# our login
em = ' '
pas = ' ' 
# click funcrion
def CLICK(a,b):
    z = driver.find_element_by_xpath(a)
    time.sleep(b)
    z.click()
# write function
def tipe(a,b,c):
    email = driver.find_element_by_xpath(a)
    time.sleep(b)
    email.click()
    time.sleep(b)
    email.send_keys(c)
# click
CLICK('//*[@id="openid-buttons"]/button[1]',0.5)
# sign in
tipe('//*[@id="identifierId"]',0.5 ,em)
CLICK('//*[@id="identifierNext"]', 0.5)
# sleep 2 second
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password"]').click()
# sleep 0.5 sec
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(pas)
CLICK('//*[@id="passwordNext"]/span/span', 0.5)
# sleep 5 second
time.sleep(5)
# google ligin complate
# open youtube
driver.get('https://music.youtube.com/')
# sleep 2 sec
time.sleep(2)
CLICK('//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-pivot-bar-renderer/ytmusic-pivot-bar-item-renderer[3]/yt-formatted-string', 0.5)
# sleep 2 sec
time.sleep(2)
# open youtube playlist
driver.get('https://music.youtube.com/playlist?list=LM')
# sleep 4 sec
time.sleep(4)
# get all links in playlist
for i in range(1 , 100):
    link = driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer['+ str(i) +']/div[2]/div[1]/yt-formatted-string/a')
    print(link.get_attribute("href"))
    musicList.append(link.get_attribute("href"))
    time.sleep(1)


# download format 
ydl_opts = {'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
# start download
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(musicList)
