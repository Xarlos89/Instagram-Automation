# Instagram-bot
 A simple instagram bot. Initial upload.

-----------------------------

Prerequisites

You must have ChromeDriver ChromeDriver 81.0.4044.69 installed.
https://chromedriver.chromium.org/downloads

You must have Google Chrome installed.
https://www.google.com/chrome/


  - Place the file "Chromedriver" in the project folder.
  - Once you have placed Chromedriver in your project folder, change the path on line 122 and 123 to your chromedriver file path.
  - Edit Secret.py to your Login credentials.
  - To change number of story views, change the number on the end of line 61.
  - To change number of likes before moving onto the next hashtag, change number on the end of line 87.


-----------------------------

Using the Instabot

- Load the application by starting a command prompt at the project folder.
- type "Python instabot.py"
- 1 = Watch Instagram Stories
  2 = Like Hashtagged posts
  3 = Exit

To change hashtags, edit hashtag_list in the Instabot.py file.
To change number of story views, change the number on the end of line 61.
To change number of likes before moving onto the next hashtag, change number on the end of line 87.

-----------------------------

Future updates

- Looking to add a menu option to edit the list of hashtags.
- Looking to add menu option to edit the amount of stories viewed.
- Looking to add menu option to edit the amount of likes per hashtag.
- Looking to add login feature at the beginning of the sequence so the
  user doesn't have to update the files by themselves.
