# Simple HuggingChat CLI

Get quick answers from HuggingChat LLMs without leaving the terminal.

## Features

This project is very barebones for now. Just the necessities:

- Login
- Send a single message and get a response (each message starts a new "conversation")
- Choose the model to use when sending a query

## Example

```
$ hugging-chat Hello, world!
Hello! How can I assist you today?
```

## Getting started

Clone this repo: `git clone https://github.com/arcanemachine/simple-hugging-chat-cli`

Then, `cd simple-hugging-chat-cli` and follow these instructions:

- Create a Python virtualenv: `python3 -m venv venv`
- Activate the virtualenv: `source venv/bin/activate`
- Install the dependencies: `pip install -r requirements.txt`
- Copy the example config template to create a (gitignored) local config file: `cp config.env.example config.env`
  - Add your email address to the config file. (It is used to log you into HuggingChat.)
- Run the login script to set cookies: `./hugging-chat-login`
  - NOTE: This will store the cookies in a (gitignored) directory in this repo (`./cookies`).
- Send a message: `./hugging-chat Hello, world!`
  - This should produce a streaming response like this to your terminal: `Hello! How can I assist you today?`

> TIP: The `hugging-chat` script activates the virtual environment automatically, so you do not need to manually activate it after initial setup. That means you can symlink the `hugging-chat` to your path for easier access.

## Configure the model

The models are configured by their name as seen in [the HuggingChat web UI Settings](https://huggingface.co/chat/settings) page (e.g. `Qwen/Qwen3-235B-A22B`).

To change the model used, change the `HUGGING_CHAT_DEFAULT_LLM` config item in `config.env`.
