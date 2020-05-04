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
  - Once you have placed Chromedriver in your project folder, change the path on line 201 and 202 to your chromedriver file path.
  - Edit Secret.py to your Login credentials.
  - To change number of story views, change the number on the end of line 67.
  - To change number of likes before moving onto the next hashtag, change number on the end of line 93.


-----------------------------

Using the Instabot

- Load the application by starting a command prompt at the project folder.
- type "Python instabot.py"
- 1 = Watch Instagram Stories
  2 = Like Hashtagged posts
  3 = Exit

To change hashtags, edit hashtag_list in the Instabot.py file OR use the built-in function. (supports copy and paste. no #-sign.)
To change number of story views, change the number on the end of line 61.
To change number of likes before moving onto the next hashtag, change number on the end of line 87.

-----------------------------
May 4, 2020
- Added functionality to update hashtag lists from the terminal.
  - clear function is broken. It will prompt you "do you want to clear?", but despite your answer will always clear the list.

- tweaked the waiting times "sleep()" to avoid crashes with slow loading pages.

Future updates
- looking to add a file read/write feature to keep hashtag list in a .txt file.
- Looking to add menu option to edit the amount of stories viewed.
- Looking to add menu option to edit the amount of likes per hashtag.
- Looking to add login feature at the beginning of the sequence so the
  user doesn't have to update the secret.py file.
