import random
import string
from selenium import webdriver

def generate_random_string(length):
  return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def create_discord_account():
  # Use Chrome as the webdriver
  driver = webdriver.Chrome()

  # Go to the Discord signup page
  driver.get('https://discord.com/register')

  # Generate a random email address
  email = f'GMAIL ADDRESS HERE+{generate_random_string(10)}@gmail.com'
  
  # Generate a random password
  password = generate_random_string(10)
  
  # Generate a random username
  username = f'USERNAME HERE{generate_random_string(10)}'
  
  # Find the email input field and enter the email
  email_field = driver.find_element_by_name('email')
  email_field.send_keys(email)
  
  # Find the password input field and enter the password
  password_field = driver.find_element_by_name('password')
  password_field.send_keys(password)
  
  # Find the username input field and enter the username
  username_field = driver.find_element_by_name('username')
  username_field.send_keys(username)
  
  # Find the signup button and click it
  signup_button = driver.find_element_by_css_selector('.app-3qnQfZ > form > button')
  signup_button.click()
  
  # Wait for the account to be created
  driver.implicitly_wait(10)
  
  # Print the login information to the terminal
  print(f'Email: {email}')
  print(f'Password: {password}')
  print(f'Username: {username}')
  
  # Close the browser
  driver.quit()

# Create a new Discord account
create_discord_account()