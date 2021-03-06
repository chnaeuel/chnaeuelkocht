# chnaeuelkocht

Quick and dirty Twitter cooking bot.

[See it in action.](https://twitter.com/hashtag/chnaeuelkocht)

## Usage

### Preparations

In order to tweet, you need to set following environment variables:

 - `CONSUMER_KEY`
 - `CONSUMER_SECRET`
 - `ACCESS_TOKEN_KEY`
 - `ACCESS_TOKEN_SECRET`

Alternatively you can also set them in a file `.env` located in the same directory as
the code:

```env
CONSUMER_KEY=secret
CONSUMER_SECRET=secret
ACCESS_TOKEN_KEY=secret
ACCESS_TOKEN_SECRET=secret
```

### General

```
usage: chnaeuelkocht [-h] [-t] [-n LINES] [--table]

optional arguments:
  -h, --help            show this help message and exit
  -t, --tweet           send tweet status
  -n LINES, --lines LINES
                        amount of lines to generate
  --table               print as table if more than one line
```
