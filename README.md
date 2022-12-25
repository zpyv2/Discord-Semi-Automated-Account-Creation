# Discord-Semi-Automated-Account-Creation
A simple script which uses webdriver to automate 95% of the discord account creation process, the 5% being the email verification (optional but reccomended) and occasional captcha.


# Initial Setup
1) Create a new gmail address if you don't want your main gmail flooded with verification emails.
2) Change only the things mentioned below unless you know what you are doing, it will mess up the script.
Go to line 16 and change GMAIL ADDRESS HERE to your new gmail, do not delete the + after HERE and before {generate_random_string
Go to line 22 and change USERNAME HERE to whatever you would like the username to be, the script adds an additional 10 random characters to the end of the username (to change, simply replace the 10 after {generate_random_string to the amount you prefer).
3) Download the webdriver apropriate to your chrome version, (lookup tutorial if you don't know how.) and place it in the same folder where main.py is located.

There you go! The only flaw is that you have to complete the captcha, but there are websites that you can pay people to do captchas for you, (like $0.05 per captcha) very useful if you are thinking about generating mass tokens for reselling, to intergrate captcha bypass, pay captcha or whatever, you will have to edit the code.


# Thanks for using my scripts!
