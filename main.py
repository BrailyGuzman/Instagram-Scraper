import os
import time
import stdiomask
try:
    import requests
    from colorama import init, Fore
except ModuleNotFoundError:
    os.system('pip install requests')
    import requests
    os.system('pip install colorama')
    from colorama import init, Fore

# os.system('clear') Mac/Linux Users
os.system('cls')
init(autoreset=True)
r = requests.Session()

class Scraper:
    def __init__(self):
        pass

    def login(self, username, password):
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "x-csrftoken": "dydX2TKkziQrOxp816zLjSyxmQYCukzC",
            "content-type": "application/x-www-form-urlencoded"
        }

        url = "https://www.instagram.com/accounts/login/ajax/"

        data = {
            "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1662950310:" + password,
            "username": username,
            "queryParams": "{}"
        }

        login = r.post(url, headers=headers, data=data)
        r.cookies = login.cookies

        if 'userId' in login.text:
            print(f"\n[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Successfully Logged In")
            time.sleep(2)
        else:
            print(f"\n[{Fore.LIGHTRED_EX}+{Fore.RESET}] Wrong Username/Password")
            time.sleep(3)
            exit()

    def scraper(self, target):
            headers = {
                "user-agent": "Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)",
                "x-csrftoken": "fbMty08hNS2evXP6EB4IsnFqoIUjGPB7"
            }

            target_info = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={target}"

            user_info = r.get(target_info, headers=headers)
            # DATA

            time.sleep(2)
            userId = user_info.json()["data"]["user"]["id"]
            username = user_info.json()["data"]["user"]["username"]
            pfp_url = user_info.json()["data"]["user"]["profile_pic_url_hd"]
            is_private = user_info.json()["data"]["user"]["is_private"]
            is_verified = user_info.json()["data"]["user"]["is_verified"]
            is_joined_recently = user_info.json()["data"]["user"]["is_joined_recently"]
            full_name = user_info.json()["data"]["user"]["full_name"]
            biography = user_info.json()["data"]["user"]["biography_with_entities"]["raw_text"]
            external_url = user_info.json()["data"]["user"]["external_url"]
            posts = user_info.json()["data"]["user"]["edge_owner_to_timeline_media"]["count"]
            followers = user_info.json()["data"]["user"]["edge_followed_by"]["count"]
            following = user_info.json()["data"]["user"]["edge_follow"]["count"]
            scraper_info = f"""
[{Fore.LIGHTGREEN_EX}userId{Fore.RESET}]: {userId}
[{Fore.LIGHTGREEN_EX}Username{Fore.RESET}]: {username}
[{Fore.LIGHTGREEN_EX}Profile Picture{Fore.RESET}]: {pfp_url}
[{Fore.LIGHTGREEN_EX}Is Private{Fore.RESET}]: {is_private}
[{Fore.LIGHTGREEN_EX}Is Verified{Fore.RESET}]: {is_verified}
[{Fore.LIGHTGREEN_EX}Is Joined Recently{Fore.RESET}]: {is_joined_recently}
[{Fore.LIGHTGREEN_EX}Full Name{Fore.RESET}]: {full_name}
[{Fore.LIGHTGREEN_EX}Biography{Fore.RESET}]: {biography}
[{Fore.LIGHTGREEN_EX}External URL{Fore.RESET}]: {external_url}
[{Fore.LIGHTGREEN_EX}Posts Count{Fore.RESET}]: {posts}
[{Fore.LIGHTGREEN_EX}Followers Count{Fore.RESET}]: {followers}
[{Fore.LIGHTGREEN_EX}Following Count{Fore.RESET}]: {following}
            """

            print(scraper_info)

scraper = Scraper()

def main():
    login_logo = f"""{Fore.LIGHTCYAN_EX}
   __             _       
  / /  ___   __ _(_)_ __  
 / /  / _ \ / _` | | '_ \ 
/ /__| (_) | (_| | | | | |
\____/\___/ \__, |_|_| |_|
            |___/          {Fore.RESET} \n
    """
    print(login_logo)
    username = input(f"[{Fore.LIGHTRED_EX}+{Fore.RESET}] Username: ")
    password = stdiomask.getpass(prompt=f"[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.RESET}Password: ", mask='*')

    scraper.login(username=username, password=password)

    # os.system('clear') Mac/Linux Users
    os.system('cls')
    while True:
        scraper_logo = f""" {Fore.LIGHTCYAN_EX}
 __                                
/ _\ ___ _ __ __ _ _ __   ___ _ __ 
\ \ / __| '__/ _` | '_ \ / _ \ '__|
_\ \ (__| | | (_| | |_) |  __/ |   
\__/\___|_|  \__,_| .__/ \___|_|   
                  |_|      {Fore.RESET} \n           
"""
        print(scraper_logo)
        target = input(f"[{Fore.LIGHTRED_EX}+{Fore.RESET}] Target: ")

        scraper.scraper(target=target)


if __name__ == '__main__':
    main()
