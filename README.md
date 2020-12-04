# Instagram-bot
 A simple instagram bot. Initial upload.
 This bot is provided for educational purposes only. I am not responsible for what you do, or what happens to your accounts when you use this bot.

-----------------------------

Prerequisites

You must have Google Chrome installed.
https://www.google.com/chrome/

You must have ChromeDriver 
I am currently using version 87.0.4280.20, however use the version that works with your version of Chrome.
https://chromedriver.chromium.org/downloads

  - Download or clone the repository to your desktop. 
  - Download the Chromedriver, unzip it and palce it in the Instagram-bot folder.
  - Once you have placed Chromedriver in your project folder, change the path on line 192 to your chromedriver file path. For example ('/Users/adam/Desktop/Instagram-bot-master/chromedriver')
  - Edit Secret.py and update it with your log-in credentials to instagram. 

-----------------------------

Using the Instabot

- Load the application by starting a command prompt in the project folder.
- type "Python instabot.py"
- To set your hashtags, edit hashtaglist.txt. Keep the format the same. 

I highly reccomend keeping your total likes to under 500 per day to not upset the Instagram gods. You've been warned. 


-----------------------------
December 4, 2020
- Updated the bot to simplify the setup process. You now only need to edit the chromedriver path. 
- The bot will now ask you how many likes and views youd like to do. 
- Updated flows to make the bot run smoother.
- Added exception passes to prevent crashes. The bot is now made of thick glass, instead of thin glass.
- Added clicks to get past cookie promt and notification prompt when you load instagram. 
- pretty colors
- updated some xpaths to respond to instagram updates.


May 12, 2020
- Updated the hashtag menu.
  - Now supports saving the hashtag list to a .txt file. (Hashtaglist.txt) You may edit the file directly, or use the built in terminal editor. Does not support using the "#" sign.
  - Now using a dictionary for the menu, updated the add and delete functions to work properly.

May 4, 2020
- Added functionality to update hashtag lists from the terminal.
- tweaked the waiting times "sleep()" to avoid crashes with slow loading pages.

Future updates

- Looking to add menu option to edit the amount of stories viewed.
- Looking to add menu option to edit the amount of likes per hashtag.
- Looking to add login feature at the beginning of the sequence so the
  user doesn't have to update the secret.py file.
