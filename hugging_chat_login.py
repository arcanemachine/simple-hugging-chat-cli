import sys

from hugchat.login import Login

email = sys.argv[1]
password = sys.argv[2]

cookie_dir_path = "./cookies/"
login_instance = Login(email, password)

cookies = login_instance.login(cookie_dir_path=cookie_dir_path, save_cookies=True)
