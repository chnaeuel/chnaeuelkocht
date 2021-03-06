#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import random
import sys
from collections import namedtuple
from pathlib import Path

import tweepy
from dotenv import load_dotenv

from data import ACTION, AMOUNT, FOOD, UNIT

dotenv_path = Path(__file__).parent.absolute() / ".env"
load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.environ.get("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")


def parse_arguments(args):
    """
    Parse all arguments.
    """
    parser = argparse.ArgumentParser(
        prog="chnaeuelkocht",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-t",
        "--tweet",
        dest="tweet",
        action="store_true",
        help="send tweet status",
    )

    parser.add_argument(
        "-n",
        "--lines",
        dest="lines",
        type=int,
        default=1,
        help="amount of lines to generate",
    )

    parser.add_argument(
        "--table",
        dest="table",
        action="store_true",
        help="print as table if more than one line",
    )

    args = parser.parse_args(args)

    if args.tweet and None in [
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN_KEY,
        ACCESS_TOKEN_SECRET,
    ]:
        parser.error(
            "For tweeting you need to set CONSUMER_KEY, CONSUMER_SECRET,"
            " ACCESS_TOKEN_KEY and ACCESS_TOKEN_SECRET environment variables."
        )

    return args


def tweet(status):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    api.update_status(status)


Element = namedtuple("Element", ["singular", "plural", "inflect"])


def get_random_element(l):
    element = random.choice(l)
    singular = element[0][0]
    plural = element[0][1] if len(element[0]) > 1 else None
    inflect = element[1]
    return Element(singular, plural, inflect)


def get_values():
    amount = random.choice(AMOUNT)

    _unit = get_random_element(UNIT)
    unit = _unit.singular if amount == 1 or not _unit.plural else _unit.plural

    _food = get_random_element(FOOD)
    food = _food.singular
    if amount > 1 and _food.plural and (_unit.inflect or _food.inflect):
        food = _food.plural

    action = random.choice(ACTION)

    if amount > 10 and unit == "kg":
        unit = "g"
    elif amount > 100 and unit in ["Meter", "cm"]:
        amount = int(amount / 10)

    return amount, unit, food, action


def get_max_lengths(status):
    lengths = {"amount": 0, "unit": 0, "food": 0, "action": 0}
    for ct, field in enumerate(["amount", "unit", "food", "action"]):
        for stat in status:
            if len(stat[ct]) > lengths[field]:
                lengths[field] = len(stat[ct])
    return lengths


def get_table(status):
    lengths = get_max_lengths(status)

    rows = []
    for value in status:
        amount, unit, food, action = value

        rows.append(
            f"{amount:<{lengths['amount']}} {unit:<{lengths['unit']}} "
            f"{food:<{lengths['food']}} {action:<{lengths['action']}}"
        )

    return "\n".join(rows)


def action(do_tweet, lines, table):
    status_list = []
    for _ in range(lines):
        amount, unit, food, action = get_values()
        status_list.append([str(amount), unit, food, action])

    status = "\n".join([" ".join(status) for status in status_list])

    if lines > 1 and table:
        status = get_table(status_list)

    status = f"{status}\n\n#chnaeuelkocht"

    print(status)

    if do_tweet:
        tweet(status)


def main():
    args = parse_arguments(sys.argv[1:])
    action(args.tweet, args.lines, args.table)


if __name__ == "__main__":  # pragma: no cover
    main()
