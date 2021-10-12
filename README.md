# kharms-bot

A modified version of the [Kierkegaard repetition bot](https://github.com/lexipenia/repetition-bot-2). Rather than insert a long string of blank characters to guarantee non-identity of tweets, this fractures the tweet by inserting random numbers of zero-width spaces between its characters.

I'm assuming that the Twitter API doesn't like this sort of thing, so am sticking with the Selenium approach, which so far has worked well for Søren.

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