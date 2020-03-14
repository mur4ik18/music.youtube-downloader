from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import youtube_dl

driver = webdriver.Chrome('chromedriver')
driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')


musicList=[]

em = ''
pas = '' 



# click funcrion
def CLICK(a,b):
    z = driver.find_element_by_xpath(a)
    time.sleep(b)
    z.click()

def tipe(a,b,c):
    email = driver.find_element_by_xpath(a)
    time.sleep(b)
    email.click()
    time.sleep(b)
    email.send_keys(c)



CLICK('//*[@id="openid-buttons"]/button[1]',0.5)

# sign in
#CLICK('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[2]', 0.5)
tipe('//*[@id="identifierId"]',0.5 ,em)
CLICK('//*[@id="identifierNext"]', 0.5)


time.sleep(2)
driver.find_element_by_xpath('//*[@id="password"]').click()
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(pas)


CLICK('//*[@id="passwordNext"]/span/span', 0.5)
time.sleep(5)
driver.get('https://music.youtube.com/')


time.sleep(2)
CLICK('//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-pivot-bar-renderer/ytmusic-pivot-bar-item-renderer[3]/yt-formatted-string', 0.5)
time.sleep(2)
driver.get('https://music.youtube.com/playlist?list=LM')
time.sleep(4)

for i in range(1 , 100):
    link = driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer['+ str(i) +']/div[2]/div[1]/yt-formatted-string/a')
    print(link.get_attribute("href"))
    musicList.append(link.get_attribute("href"))
    time.sleep(1)



ydl_opts = {'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(musicList)
