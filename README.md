# Instagram-bot
 A simple instagram bot. Initial upload.
 This bot is provided for educational purposes only. I am not responsible for what you do, or what happens to your accounts when you use this bot.

-----------------------------

Prerequisites

You must have ChromeDriver ChromeDriver 81.0.4044.69 installed.
https://chromedriver.chromium.org/downloads

You must have Google Chrome installed.
https://www.google.com/chrome/


  - Place the file "Chromedriver" in the project folder.
  - Once you have placed Chromedriver in your project folder, change the path on line 187 and 188 to your chromedriver file path.
  - Edit line 85 to the path of Hashtaglist.txt
  - Edit Secret.py to your Login credentials.
  - To change number of story views, change the number on the end of line 68.
  - To change number of likes before moving onto the next hashtag, change number on the end of line 95.

-----------------------------

Using the Instabot

- Download or clone the repository to your desktop. 
- Download the Chromedriver and place this in the repository folder. https://chromedriver.chromium.org/downloads
  - Once you have placed Chromedriver in your project folder, change the path on line 201 and 202 to your chromedriver file path.
- Edit Secret.py to your Login credentials.
- Load the application by starting a command prompt at the project folder.
- type "Python instabot.py"


- To change hashtags, edit hashtaglist.txt OR use the built-in function. (supports copy and paste. no #-sign.)
- To change number of story views, change the number on the end of line 68.
- To change number of likes before moving onto the next hashtag, change number on the end of line 95.

-----------------------------
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
