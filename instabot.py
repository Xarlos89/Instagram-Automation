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

print('=======================================================')
print('==========*                                 *==========')
print('==========*                                 *==========')
print('==========*         Instagram Bot           *==========')
print('==========*                                 *==========')
print('==========*                                 *==========')
print("==================     By: Adam     ===================")
print("==================    Version 5.0    ==================")
sleep(1)
print("=============== Loading magic stuff... ================")
for i in tqdm(range(100)):
     sleep(0.01)
     pass

def menu():
    menu = {}
    menu['1'] = "Watch Instagram Stories"
    menu['2'] = "Like Hashtagged posts"
    menu['3'] = "Edit hashtag list"
    menu['4'] = "Exit"
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
            break
        else:
            print("\nYou have to choose an option between 1 and 4. \n")
            menu()

def watchstories():
    sleep(1)
    webdriver.find_element_by_xpath('//div[contains(text(), "Watch All")]').click() # click on the tab where the stories are
    stories_watched = 0
    sleep(2)
    try:
        while webdriver.find_element_by_class_name('coreSpriteRightChevron') and stories_watched < 200: # value modifies how many stories you want to watch
            webdriver.find_element_by_class_name('coreSpriteRightChevron').click() # Clicks next story.
            sleep(randint(1, 2)) # Random timer to skip through stories.
            stories_watched += 1
            print("stories watched: {}".format(stories_watched))
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
        loadstories = 0
    except:
        print('\033[0;33mEND! No more stories to view\033[m')
        loadstories = 0
    webdriver.find_element_by_class_name('Szr5J').click()
    menu()

def likes():
    likes = 0
    tag = -1
    hashtag_list = open('***** PATH TO HASHTAGLIST.txt *****').readlines()
    for hashtag in hashtag_list:
        tag = tag+1
        print('Liking the hashtag: ' + hashtag_list[tag])
        webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
        image_img=webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')
        sleep(1)
        image_img.click()
        sleep(1)
        likes = 0
        while (likes <= 1): #Set max amount of likes
            sleep(1)
            image_like_svg=webdriver.find_element_by_css_selector('.fr66n > button:nth-child(1) > svg:nth-child(1)')
            image_like_label=image_like_svg.get_attribute("aria-label")
            if image_like_label == "Like":
                sleep(2)
                image_like_svg.click()
                likes += 1
                print('liked images: {}'.format(likes))
                sleep(randint(4, 9))
                image_next = webdriver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                image_next.click()
                print("Looking for image...")
                sleep(randint(4, 7))
            else:
                print('Image already liked')
                image_next = webdriver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                image_next.click()
                sleep(1)
        else:
            sleep(2)
            print('finished with the hashtag: ' + hashtag_list[tag])
            image_close=webdriver.find_element_by_class_name('wpO6b')
            sleep(2)
            image_close.click()
            sleep(2)
        print("Finished liking hashtag: " + hashtag_list[tag])
        sleep(1)
    print("Finished liking all hashtags in the hashtag list.")
    webdriver.get('https://www.instagram.com/')
    sleep(2)
    menu()

######################################################################################################
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
        userinput = input("What hastag would you like to delete? ")
        for line in list:
            if line.strip("\n") != userinput:
                f.write(line)

######################################################################################################

## Open Selenium Webdriver
chromedriver_path = '/Users/adammiranda-artizada/Desktop/Python/Projects/Instabot/Instabot (working file)/chromedriver'  # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path="/Users/adammiranda-artizada/Desktop/Python/Projects/Instabot/Instabot (working file)/chromedriver")# Change this one too
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

sleep(3)
### Log in
username = webdriver.find_element_by_name('username')
username.send_keys(secret.username)
password = webdriver.find_element_by_name('password')
password.send_keys(secret.password)
sleep(2)
button_login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button')
button_login.click()

sleep(6)
### next 3 lines are for notification box, remove if you dont get the box
notnow = webdriver.find_element_by_css_selector('button.aOOlW:nth-child(2)')
notnow.click()
menu()

sleep(2)
