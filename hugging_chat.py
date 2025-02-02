#!/usr/bin/env python3

import os
import sys

from hugchat import hugchat
from hugchat.login import Login

def get_chatbot_instance():
    # Configurable items
    default_llm = os.environ.get("HUGGING_CHAT_DEFAULT_LLM", "Qwen/Qwen2.5-72B-Instruct")
    email = os.environ["HUGGING_CHAT_EMAIL"]

    # Set up cookies
    cookie_dir_path = "./cookies/"
    cookies = Login(email).load_cookies(cookie_dir_path)

    return hugchat.ChatBot(
        cookies=cookies.get_dict(),
        default_llm=default_llm)

def send_message(chatbot, message):
    for resp in chatbot.chat(message, stream=True):
        if resp is not None:
            # Print each token to the terminal as the response is streamed
            sys.stdout.write(resp["token"])
            sys.stdout.flush()
        else:
            print()
            sys.exit(0)

if __name__ == "__main__":
    chatbot = get_chatbot_instance()
    message = sys.argv[1]

    send_message(chatbot, message)
