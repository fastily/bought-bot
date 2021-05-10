#!/usr/bin/env bash

cd "${0%/*}" &> /dev/null

if ! command -v brew &> /dev/null; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

if [ $(sysctl -n machdep.cpu.brand_string) == "Apple M1" ]; then # TODO: zsh compatability
    cat >> ~/.bash_profile <<- 'EOF'
        for d in "/opt/homebrew/sbin" "/opt/homebrew/bin"; do
            if [ -d "$d" ]; then
                    export PATH="${d}:${PATH}"
            fi
        done
EOF

    export "PATH=/opt/homebrew/sbin:/opt/homebrew/bin:${PATH}"
fi

brew install bash python
brew install --cask chromedriver google-chrome

pip3 install virtualenv
virtualenv venv_bought_bot
venv_bought_bot/bin/pip install -r requirements.txt
