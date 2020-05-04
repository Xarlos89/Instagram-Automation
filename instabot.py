import os
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
import sys
sys.path.insert(0, './utils/')
import secret

print('=======================================================')
print('==========*                                 *==========')
print('==========*                                 *==========')
print('==========*         Instagram Bot           *==========')
print('==========*                                 *==========')
print('==========*                                 *==========')
print("==================     By: Adam     ===================")
print("==================    Version 4.0    ==================")
sleep(2)
print("=============== Loading magic stuff... ================")
for i in tqdm(range(100)):
    sleep(0.01)
    pass

hashtag_list = ['insert', 'hashtags', 'here', 'like', 'this']

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
            watchstories()
        elif selection == '2':
            likes()
        elif selection == '3':
            os.system('clear')
            hashtag_menu()
        elif selection == '4':
            os.system('clear')
            break
        else:
            print("You have to choose an option between 1 and 4. ")

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
        print('\033[0;33mEND! No more stories to watch\033[m')
        loadstories = 0
    webdriver.find_element_by_class_name('Szr5J').click()
    menu()

def likes():
    likes = 0
    tag = -1
    for hashtag in hashtag_list:
        tag = tag+1
        print('Liking the hashtag: ' + hashtag_list[tag])
        webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
        image_img=webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')
        sleep(1)
        image_img.click()
        sleep(1)
        likes = 0
        while (likes <= 9): #Set max amount of likes. 9 will like a hashtag 10 times.
            sleep(1)
            image_like_svg=webdriver.find_element_by_css_selector('.fr66n > button:nth-child(1) > svg:nth-child(1)')
            image_like_label=image_like_svg.get_attribute("aria-label")
            if image_like_label == "Like":
                sleep(2)
                image_like_svg.click()
                likes += 1
                print('liked images: {}'.format(likes))
                sleep(randint(5, 7))
                image_next = webdriver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                image_next.click()
                print("Looking for image...")
                sleep(randint(4, 5))
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
    print("Finished liking all hashtags in the hashtag list.")
    webdriver.get('https://www.instagram.com/')
    sleep(2)
    menu()

################################################### Changing Hashtag list update. Need to add write-to-file functionality.

def makehashlist(new_tag):
    os.system('clear')
    hashtag_list.append(new_tag)
    print("\n====================")
    for tag in hashtag_list:
        print(tag)
    print("\n====================")
    print("\nAdded {}. List now has {} hashtags.".format(new_tag, len(hashtag_list)))
    sleep(1)

def show_list():
    os.system('clear')
    print("Current hashtag list: ")
    print("\n====================")
    for tag in hashtag_list:
        print(tag)
    print("\n====================")
    sleep(1)

def deletetag():
    os.system('clear')
    print("\n====================")
    for tag in hashtag_list:
        print(tag)
    print("\n====================")
    delete_tag = input("\nWhich hashtag would you like to remove from the list? ")
    hashtag_list.remove(delete_tag)
    os.system('clear')
    for tag in hashtag_list:
        print(tag)
    print("\n{} has been removed form the hashtag list.".format(delete_tag))
    sleep(1)

def clearHashtags():
    os.system('clear')
    print("\n====================")
    for tag in hashtag_list:
        print(tag)
    print("\n====================")
    clear_tags = input("\nWould you like to erase your hashtag list?")
    if clear_tags.lower() == 'yes' or 'y':
        print("Hashtag list erased...")
        del hashtag_list[:]
    else:
        print("Did not delete hashtag list.")

def hashtag_menu():
    print("\n====================")
    for tag in hashtag_list:
        print(tag)
    print("====================")
    print("\n\nEnter 'done' to save your list and go back to the main menu.")
    print("Enter 'show' to see your list.")
    print("Enter 'delete' to remove a tag from your list.")
    print("Enter 'clear' to erase your list.")
    while True:
        new_tag = input("\n\nEnter a tag: ")

        if new_tag == 'done'.lower():
            os.system('clear')
            break
        elif new_tag == 'show'.lower():
            show_list()
            continue
        elif new_tag == 'delete'.lower():
            show_list()
            deletetag()
            continue
        elif new_tag == 'clear'.lower():
            clearHashtags()
            continue
        makehashlist(new_tag)
    menu()

### Open Selenium Webdriver
chromedriver_path = '/Users/Desktop/Instabot/chromedriver'  # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path="/Users/Desktop/Instabot/chromedriver")# Change this one too
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
