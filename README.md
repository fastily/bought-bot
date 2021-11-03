# bought-bot
[![Python 3.9+](https://upload.wikimedia.org/wikipedia/commons/4/4f/Blue_Python_3.9%2B_Shield_Badge.svg)](https://www.python.org)
[![License: GPL v3](https://upload.wikimedia.org/wikipedia/commons/8/86/GPL_v3_Blue_Badge.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

Bot for buying things on websites, to give non-scalpers a fighting chance.  Currently only works with Best Buy.

## Dependencies
* [Python](https://www.python.org)
* [Chrome](https://www.google.com/chrome/)
* [chromedriver](https://chromedriver.chromium.org)

Use latest versions of each for best results.

## Run
Copy the contents of `blank_config.ini` and save it in a new file, `config.ini`,  in the the bought_bot directory.  Fill in the form in `config.ini`, and be sure you have saved a credit card in your account details online.

* Set `url = ` to the url of the item to purchase
* Set `live = True` if you want the bot to actually try purchasing something.  To perform a dry run (do everything except purchase), leave this field blank.

Running the program:
```bash
# from source
python -m bought_bot

# installed with pip
bought_bot
```

## Note
Sometimes Best Buy will randomly prompt the user for SMS 2FA.  Not entirely sure why this happens, but bypassing this is not yet supported.