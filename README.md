## AutoReply

Comments on every new submission or comment on a chosen subreddit.

### Instructions

-   Install requirements `pip install -r requirements.txt`
-   Create Reddit (script) app at <https://www.reddit.com/prefs/apps/> and get keys
-   Edit conf.ini with your details
-   Run it `python run.py`

### Settings Info

-   `target_subreddit` - Bot account must be mod
-   `target_keywords` - Kewwords to search for (separated by commas)
-   `reply_texts` - Texts to reply with (separated by commas)

### Help

    usage: run.py [-h] [-t] [-s] [-c] [-d]

    AutoReply v2 (by /u/impshum)

    optional arguments:
      -h, --help         show this help message and exit
      -t, --test         test mode
      -s, --submissions  reply to submissions
      -c, --comments     reply to comments
      -d, --delete       delete saved ids

### Notes

-   If you're not using Unix you won't see the colours in the terminal (command prompt). Follow [THIS](https://recycledrobot.co.uk/words/?print-python-colours) tutorial to get them working.
-   I will not be held responsible for any bad things that might happen to you or your Reddit account whilst using this bot. Follow Reddiquette and stay safe.

### Tip

BTC - 1AYSiE7mhR9XshtS4mU2rRoAGxN8wSo4tK
