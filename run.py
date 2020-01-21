import praw
import time
import configparser


class C:
    W, G, R, P, Y, C = '\033[0m', '\033[92m', '\033[91m', '\033[95m', '\033[93m', '\033[36m'


def main():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    target_subreddit = config['SETTINGS']['target_subreddit']
    reply_text = config['SETTINGS']['reply_text']
    test_mode = config['SETTINGS'].getboolean('test_mode')

    tm = ''
    if test_mode:
        tm = f'{C.R}TEST MODE{C.Y}'

    print(f"""{C.Y}
╔═╗╦ ╦╔╦╗╔═╗╦═╗╔═╗╔═╗╦ ╦ ╦
╠═╣║ ║ ║ ║ ║╠╦╝║╣ ╠═╝║ ╚╦╝ {tm}
╩ ╩╚═╝ ╩ ╚═╝╩╚═╚═╝╩  ╩═╝╩  {C.C}v1.0 {C.G}impshum{C.W}
    """)

    reddit = praw.Reddit(
        username=config['REDDIT']['reddit_user'],
        password=config['REDDIT']['reddit_pass'],
        client_id=config['REDDIT']['client_id'],
        client_secret=config['REDDIT']['client_secret'],
        user_agent='Autoreply (by u/impshum)'
    )

    start_time = time.time()

    for submission in reddit.subreddit(target_subreddit).stream.submissions():
        if submission.created_utc > start_time:
            if not test_mode:
                submission.reply(reply_text)
            print(f'{C.G}Commented on {submission.title}{C.W}')


if __name__ == "__main__":
    main()
