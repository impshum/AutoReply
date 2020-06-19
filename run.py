import praw
import configparser
import argparse
import random


parser = argparse.ArgumentParser(
    description='AutoReply v2 (by /u/impshum)')
parser.add_argument(
    '-t', '--test', help='test mode', action='store_true')
parser.add_argument(
    '-s', '--submissions', help='reply to submissions', action='store_true')
parser.add_argument(
    '-c', '--comments', help='reply to comments', action='store_true')
parser.add_argument(
    '-d', '--delete', help='delete saved ids', action='store_true')
args = parser.parse_args()

test_mode = False

if args.test:
    test_mode = True

config = configparser.ConfigParser()
config.read('conf.ini')
target_subreddit = config['SETTINGS']['target_subreddit']
target_keywords = config['SETTINGS']['target_keywords']
target_keywords = [x.strip(' ') for x in target_keywords.split(',')]
reply_texts = config['SETTINGS']['reply_text']
reply_texts = [x.strip(' ') for x in reply_texts.split(',')]

reddit = praw.Reddit(
    username=config['REDDIT']['reddit_user'],
    password=config['REDDIT']['reddit_pass'],
    client_id=config['REDDIT']['client_id'],
    client_secret=config['REDDIT']['client_secret'],
    user_agent='Autoreply v2 (by u/impshum)'
)


class C:
    W, G, R, P, Y, C = '\033[0m', '\033[92m', '\033[91m', '\033[95m', '\033[93m', '\033[36m'


def process_id(id):
    with open('data.txt') as f:
        data = f.read()
    if id not in data:
        with open('data.txt', 'a') as f:
            f.write(id + '\n')
        return True


def process_text(body):
    for target_keyword in target_keywords:
        if target_keyword in body:
            return True


def main():
    if args.submissions:
        for submission in reddit.subreddit(target_subreddit).stream.submissions(skip_existing=True):
            body = submission.title.lower()
            id = submission.id
            if process_id(id):
                if process_text(body):
                    if not test_mode:
                        submission.reply(random.choice(reply_texts))
                    print(f'{C.G}{body}{C.W}')
    elif args.comments:
        for comment in reddit.subreddit(target_subreddit).stream.comments(skip_existing=True):
            body = comment.body.lower()
            id = comment.id
            if process_id(id):
                if process_text(body):
                    if not test_mode:
                        comment.reply(random.choice(reply_texts))
                    print(f'{C.G}{body}{C.W}')

    elif args.delete:
        with open('data.txt', 'w') as f:
            f.write('')
    else:
        print(f'{C.Y}Choose between comments (-c) or submissions (-s){C.W}')


if __name__ == "__main__":
    main()
