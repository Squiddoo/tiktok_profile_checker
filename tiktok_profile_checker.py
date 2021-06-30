#author: Squidward#1000
#reason: To improve my python skills

from colorama import Fore, Back, Style
import os,time
clear = lambda: os.system('cls')  
from selenium import webdriver, common
path = "/Users/Gebruiker/Desktop/chromedriver91_win32/chromedriver.exe"


print('''
___  ___          _        _                                                         
|  \/  |         | |      | |           _                                             
| .  . | __ _  __| | ___  | |__  _   _ (_)                                            
| |\/| |/ _` |/ _` |/ _ \ | '_ \| | | |                                              
| |  | | (_| | (_| |  __/ | |_) | |_| | _                                             
\_|  |_/\__,_|\__,_|\___| |_.__/ \__,  (_)                                            
                                  __/ |                                              
                                 |___/                                               
                                                                                     
                                                                                                                                             
                                                                                     
                                                                                     
 _____             _     _                       _   _  _    __  _____  _____  _____ 
/  ___|           (_)   | |                     | |_| || |_ /  ||  _  ||  _  ||  _  |
\ `--.  __ _ _   _ _  __| |_      ____ _ _ __ __| |_  __  _|`| || |/' || |/' || |/' |
 `--. \/ _` | | | | |/ _` \ \ /\ / / _` | '__/ _` |_| || |_  | ||  /| ||  /| ||  /| |
/\__/ / (_| | |_| | | (_| |\ V  V / (_| | | | (_| |_  __  _|_| |\ |_/ /\ |_/ /\ |_/ /
\____/ \__, |\__,_|_|\__,_| \_/\_/ \__,_|_|  \__,_| |_||_|  \___/\___/  \___/  \___/ 
          | |                                                                        
          |_|                                                                                                                                            
''')
time.sleep(4)
clear()
seed_name = input("[>] Enter the username you want to check: ")
full_url = "https://www.tiktok.com/@" + (seed_name)
driver = webdriver.Chrome(path)
driver.set_window_position(-10000,0)
driver.get(full_url)
time.sleep(0.5)
clear()
print("Loading data...")
time.sleep(0.2)
print("Loading data....")
time.sleep(0.2)
print("Loading data...")
clear()




element_username = driver.find_element_by_css_selector("h2.share-title")
time.sleep(0.1)
element_subuser = driver.find_element_by_css_selector("h1.share-sub-title")
time.sleep(0.1)
element_bio = driver.find_element_by_css_selector("h2.share-desc.mt10")
time.sleep(0.1)


element_followers = driver.find_element_by_css_selector("#main > div.jsx-3867589354.main-body.page-with-header.middle.em-follow > div.jsx-1013916525.share-layout.compact.middle > div > header > h2.count-infos > div:nth-child(2) > strong")
element_following = driver.find_element_by_css_selector("#main > div.jsx-3867589354.main-body.page-with-header.middle.em-follow > div.jsx-1013916525.share-layout.compact.middle > div > header > h2.count-infos > div:nth-child(1) > strong")
element_totallikes = driver.find_element_by_css_selector("#main > div.jsx-3867589354.main-body.page-with-header.middle.em-follow > div.jsx-1013916525.share-layout.compact.middle > div > header > h2.count-infos > div:nth-child(3) > strong")



print("username:", "@" + element_username.text)
print("")

if driver.find_elements_by_css_selector('#main > div.jsx-3867589354.main-body.page-with-header.middle.em-follow > div.jsx-1013916525.share-layout.compact.middle > div > header > div.share-info > div.share-title-container > h2 > svg'):
  print(Fore.GREEN + "Verified: Yes")
  print(Style.RESET_ALL)
else:
  print(Fore.RED + "Verified: No")
  print(Style.RESET_ALL)
  
print("sub-user:",element_subuser.text)
print("")
print("bio:",element_bio.text)
print("")
print("Followers:",element_followers.text)
print("Total Likes:",element_totallikes.text)
print("Following:",element_following.text)
print("")
print("[!] successfully loaded data for username: @"+ seed_name)
print("")
print(Fore.BLUE + "You may close this window now!")