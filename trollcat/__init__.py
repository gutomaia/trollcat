import sys
import argparse
import subprocess
import importlib
import logging

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger = logging.getLogger('trollcat')
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

def execute(func, *args, **kwargs):
    script = func()
    script(*args, **kwargs)

def get_script(module, script):
    def wrapper(*args, **kwargs):
        m = importlib.import_module(module)
        func = getattr(m, script)
        return func
    return wrapper

def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="trollcat",
        description='Trollcat Tweetstorm',
        epilog='')

    parser.add_argument('-r', '--reply', metavar='reply')
    parser.add_argument('-d', '--debug', metavar='debug')

    subparsers = parser.add_subparsers(
        title="subcommands", description="utilities", help="aditional help")

    # tweet_cmd = subparsers.add_parser('tweet')
    # tweet_cmd.set_defaults(func=get_script('trollcat.scripts.tweet','tweet'))

    storm_cmd = subparsers.add_parser('storm')
    storm_cmd.set_defaults(func=get_script('trollcat.scripts.storm','storm'))

    config = ConfigParser()
    config.read('config.ini')

    params = { k[0]:k[1] for k in config.items('trollcat')}
    args = parser.parse_args(argv[1:])

    params.update(vars(args))

    execute(**params)
