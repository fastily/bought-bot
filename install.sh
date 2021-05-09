#!/usr/bin/env bash

cd "${0%/*}" &> /dev/null

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install python
brew install --cask chromedriver

pip3 install virtualenv
virtualenv venv_bought_bot
venv_bought_bot/bin/pip install -r requirements.txt
