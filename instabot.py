import os
import sys
import pandas as pd
import random
from random import randint
from time import sleep, strftime
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from tqdm import tqdm_gui
sys.path.insert(0, './utils/')
import secret

print('\033[0;33m=======================================================\033[m')
print('\033[0;33m==========*                                 *==========\033[m')
print('\033[0;33m==========*                                 *==========\033[m')
print('\033[0;33m==========*\033[m         Instagram Bot           \033[0;33m*==========\033[m')
print('\033[0;33m==========*                                 *==========\033[m')
print('\033[0;33m==========*                                 *==========\033[m')
print("\033[0;33m==================\033[m     By: Adam     \033[0;33m===================\033[m")
print("\033[0;33m==================\033[m  Version 6.9.420 \033[0;33m===================\033[m")
sleep(1)
print("\033[0;33m===============\033[m Loading magic stuff... \033[0;33m================\033[m")


def menu():
    menu = {}
    menu['1'] = "\033[0;33mWatch Instagram Stories\033[m"
    menu['2'] = "\033[0;33mLike Hashtagged posts\033[m"
    menu['3'] = "\033[0;33mEdit hashtag list\033[m"
    menu['4'] = "\033[0;33mExit\033[m"
    while True:
        options = menu.keys()
        for entry in options:
            print (entry, menu[entry])

        selection = str(input("What would you like to do? "))
        if selection == '1':
            os.system('clear')
            watchstories()
        elif selection == '2':
            os.system('clear')
            likes()
        elif selection == '3':
            os.system('clear')
            hashtag_menu()
        elif selection == '4':
            os.system('clear')
            webdriver.close()
            sys.exit()
        else:
            print("\nYou have to choose an option between 1 and 4. \n")
            menu()

def watchstories():
    numStoriesToWatch = int(input('\033[0;33mHow many stories should we watch?\033[m ')) # value modifies how many stories you want to watch
    sleep(1)
    webdriver.find_element_by_css_selector('#react-root > section > main > section > div > div.zGtbP.IPQK5.VideM > div > div > div > div > ul > li:nth-child(3) > div > button > div.RR-M-.QN629 > span').click() # click on the tab where the stories are
    sleep(1)
    stories_watched = 0
    sleep(1)
    try:
        while (stories_watched != numStoriesToWatch):
            webdriver.find_element_by_css_selector('#react-root > section > div.Igw0E.rBNOH.YBx95.vwCYk > div > section > div > button.FhutL > div').click() # Clicks next story.
            stories_watched += 1
            print("\033[0;33mstories watched:\033[m {}".format(stories_watched))
            sleep(randint(1, 3)) # Random timer to skip through stories.
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
        loadstories = 0
    except:
        print('\033[0;33mNo more stories to view\033[m')
        loadstories = 0
    print("\033[0;33mFinished watching\033[m {} \033[0;33mstories\033[m".format(stories_watched))
    goHome()
    menu()

def likes():
    hashtag_list = open ("hashtaglist.txt").readlines()
    tag = -1
    goalLikes= int(input('\033[0;33mHow many likes should we do in each hashtag?:\033[m '))
    for hashtag in hashtag_list:
        currentLikes = 0
        tag = tag+1
        print('\033[0;33mLiking the hashtag:\033[m ' + hashtag_list[tag])
        webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
        image_img=webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')
        sleep(1)
        image_img.click()
        sleep(1)
        try:
            while (currentLikes != goalLikes):
                sleep(3)
                image_like_svg = webdriver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
                image_like_label = image_like_svg.get_attribute("aria-label")
                if image_like_label == "Like":
                    image_like_svg.click()
                    currentLikes += 1
                    print('Liked images: \033[0;33m{}\033[m'.format(currentLikes))
                    print("Looking for image...")
                    sleep(randint(3, 7))
                    image_next = webdriver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                    image_next.click()
                elif image_like_label == "Unlike":
                    print('\033[0;33mImage already liked.\033[m')
                    image_next = webdriver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                    image_next.click()
                    sleep(randint(1, 4))
            else:
                sleep(5)
                image_next = webdriver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                image_next.click()
                sleep(1)
        except:
            print('Oops, Instagram is having trouble in this tag, lets go to the next one. ')
            image_next = webdriver.find_element_by_class_name('coreSpriteRightPaginationArrow')
            image_next.click()
            continue
        print("\033[0;33mFinished liking hashtag:\033[m " + hashtag_list[tag])
        sleep(1)
    print("\033[0;33mFinished liking all hashtags in the hashtag list.\033[m")
    goHome()
    sleep(2)
    menu()

def hashtag_menu():
    menu2 = {}
    menu2['1'] = "Add hashtag to hashtag list"
    menu2['2'] = "Show hashtag list"
    menu2['3'] = "Delete hashtags from hashtag list"
    menu2['4'] = "Done. Go back to main menu"
    while True:
       options2 = menu2.keys()
       for entry2 in options2:
           print (entry2, menu2[entry2])

       selection2 = str(input("What would you like to do? "))
       if selection2 == '1':
           add_tag()
       elif selection2 == '2':
           show_list()
       elif selection2 == '3':
           deletetag()
       elif selection2 == '4':
           os.system('clear')
           menu()
       else:
           print("\nYou must choose an option between 1 and 4.\n")
           hashtag_menu()

def add_tag():
    with open("hashtaglist.txt", "a") as hashtaglist:
        hashtaglist.write(input("What tag would you like to add?: "))
        hashtaglist.write("\n")
    print("\nAdded tag.")
    sleep(1)

def show_list():
    os.system('clear')
    file = open("hashtaglist.txt", "r")
    print("Current hashtag list: ")
    print("\n====================\n")
    for tag in file:
        print(tag)
    print("\n====================\n")
    sleep(1)

def deletetag():
    with open("hashtaglist.txt", "r") as f:
        list = f.readlines()
        print("\nCurrent hastag list.")
        for line in list:
            print(line.strip("\n"))
        print("\n")
    with open("hashtaglist.txt", "w+") as f:
        userinput = input("What hashtag would you like to delete? ")
        for line in list:
            if line.strip("\n") != userinput:
                f.write(line)
                
def goHome():
    webdriver.get('https://www.instagram.com/')
    sleep(3)

## Open Selenium Webdriver
chromedriver_path = '************* REPLACE THIS TEXT WITH CHROMEDRIVER FILE PATH *******'  # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path= chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
for i in tqdm(range(100)):
    sleep(0.02)
try: ### This accepts the cookies offered by instagram
    acceptCookies = webdriver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
    acceptCookies.click()
    sleep(1)
except:
    pass

### Log in
usernameEntry = webdriver.find_element_by_name('username')
usernameEntry.clear()
usernameEntry.send_keys(secret.username)
passwordEntry = webdriver.find_element_by_name('password');
passwordEntry.send_keys(secret.password)
sleep(2)
button_login = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
button_login.click()

sleep(6)
### next 3 lines are for notification box, remove if you dont get the box
try:
    notnow = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    notnow.click()
    sleep(5)
except:
    pass
try:
    notifications = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    notifications.click()
except:
    print('No notification prompt to close, youre fine.')
menu()
sleep(2)
