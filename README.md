 # Instagram Poster

MOST LIKELY DEPRECATED!! (feel free to give it a try and see if it works)
 
Post your pictures on instagram! Bypasses the lack of API by using selenium and using a web browser to post on instagram.
 
This repo has 2 files: login.py and post.py. Both have one and only one method each:
```py
login(user_username, user_pwd, driver)
# Has to be called first, before post!
# Give it your instagram username, password, and a selenium webdriver instance.

post(driver, caption, paths, postDay="now", postHour = "now", postMinute = "0")
# First is your webdriver, which is the same as login. Then, the caption for your post,
# a list of the path(s) (single posts should be in a list anyways, yes, you can do carousel posts.)
# then, input, if wanted, the time at which you want to post
# (day is on the format dd/mm/yyyy and hour is base 24).
```
