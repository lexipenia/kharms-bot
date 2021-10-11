# kharms-bot

A modified version of the [Kierkegaard repetition bot](https://github.com/lexipenia/repetition-bot-2). Rather than insert a long string of blank characters to guarantee non-identity of tweets, this bot uses two space characters and places them between the words. The real non-identity them comes from random numbers of zero-width spaces. (Twitter strips blank strings at the end of tweets, so putting the spaces there won't work.)

## `config.py` and `chromedriver` location

The bot assumes that the appropriate version of [chromedriver](https://chromedriver.chromium.org/downloads) is installed at `/usr/local/bin/chromedriver`.

A `config.py` file in the same directory as the bot must be supplied, containing:
* The root of the path where `/chrome` and `/debug` directories will be created
* The desired Twitter login credentials

Example `config.py` file:
```
# choose how to extend the path for saving files (remote = absolute, for cronjob)
path_extensions = {
  "local": "./",
  "remote": "/home/<user>/kharms-bot/"
}

# Twitter login credentials
username = ""
password = ""
email = ""
phone = ""
```

## Dependencies
```
pip install selenium
```