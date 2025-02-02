# Simple HuggingChat CLI

Talk to HuggingChat LLMs without leaving the terminal.

## Features

This project is very barebones for now. Just the necessities:

- Login
- Send a single message and get a response (Each message starts a new "conversation".)
- Choose the model to use when sending a query

## Example

```
$ hugging-chat Hello, world!
Hello! How can I assist you today?
```

## Getting started

Clone this repo: `git clone https://github.com/arcanemachine/simple-hugging-chat-cli`

Then, `cd simple-hugging-chat-cli` and run the following instructions:

- Create a Python virtualenv: `python3 -m venv venv`
- Activate the virtualenv: `source venv/bin/activate`
- Install the dependencies: `pip install -r requirements.txt`
- Copy the example config template to create a (gitignored) local config file: `cp config.env.example config.env`
  - Add your email address to the config file. (It is used to log you into HuggingChat.)
- Run the login script to set cookies: `./hugging-chat-login`
  - NOTE: This will store the cookies in a (gitignored) directory in this repo (`./cookies`).
- Send a message: `./hugging-chat Hello, world!`

## Configure the model

The models are configured by their name as seen in [the HuggingChat web UI Settings](https://huggingface.co/chat/settings) page (e.g. `Qwen/Qwen2.5-72B-Instruct`).

To change the model used, change the `HUGGING_CHAT_DEFAULT_LLM` config item in `config.env`.
