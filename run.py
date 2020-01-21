import glob
import praw
import schedule
import frontmatter
import configparser
from time import sleep
from random import choice
from datetime import datetime


class C:
    W, G, R, P, Y, C = '\033[0m', '\033[92m', '\033[91m', '\033[95m', '\033[93m', '\033[36m'


config = configparser.ConfigParser()
config.read('conf.ini')
reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
client_id = config['REDDIT']['client_id']
client_secret = config['REDDIT']['client_secret']
target_subreddit = config['SETTINGS']['target_subreddit']
schedule_times = config['SETTINGS']['schedule_times']
schedule_times = schedule_times.split(',')
test_mode = config['SETTINGS'].getboolean('test_mode')


tm = ''
if test_mode:
    tm = f'{C.R}TEST MODE{C.Y}'


print(f"""{C.Y}
╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╔╗ ╔═╗╔╦╗
╚═╗╠═╝╠╦╝║ ║║║║║ ║╠╩╗║ ║ ║  {tm}
╚═╝╩  ╩╚═╚═╝╩ ╩╚═╝╚═╝╚═╝ ╩  {C.C}v1.0 {C.G}impshum{C.W}
""")


reddit = praw.Reddit(
    username=reddit_user,
    password=reddit_pass,
    client_id=client_id,
    client_secret=client_secret,
    user_agent='SPROMOBOT (by u/impshum)'
)


def get_reddit_post():
    fname = choice(glob.glob('posts/*.md'))
    with open(fname) as f:
        post = frontmatter.load(f)
    return {'title': post['title'], 'selftext': post.content}


def runner():
    post = get_reddit_post()
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    if not test_mode:
        reddit.subreddit(target_subreddit).submit(
            post['title'], selftext=post['selftext'])
        print(f'{C.P}{date_time} {C.G}Posted{C.W}')
    else:
        print(f'{C.P}{date_time} {C.G}Posted {C.R}TEST MODE{C.W}')


def main():
    for schedule_time in schedule_times:
        schedule_time = schedule_time.strip()
        schedule.every().day.at(schedule_time).do(runner)

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    main()
