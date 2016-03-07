import requests
from requests_oauthlib import OAuth1
import cnfg
import json
from pymongo import MongoClient

def into_mongo(collection, results):
    """Insert twitter results into mongoDB."""
    coll = collection
    for tweet in results:
        coll.insert_one(tweet)

def get_tweets(screen_name, since_id, call = 1, max_id = None, tweets = []):
    """Get tweets by screen name up until max tweets.
    Args:
    screen_name (str): screen name to get tweets for
    since_id (int): get tweets more recent than this specified ID
    Returns:
    json object/list with tweets and associated data
    """
    if call > max_calls:
        return tweets
    print call
    search_params = {'screen_name': [screen_name],
                     'count': 200,
                     'max_id': max_id,
                     'since_id' : since_id}
    json = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json',
                    params = search_params,
                    auth = oauth).json()
    last_id = json[-1]['id']
    try: # catches the first instance
        if tweets[-1]['id'] == last_id: # check if we ran out of tweets
            return tweets
        else:
            return tweets + get_tweets(screen_name, since_id, call + 1, last_id, json)
    except:
        return tweets + get_tweets(screen_name, since_id, call + 1, last_id, json)

def main():
    # define twitter authentication keys
    config = cnfg.load(".twitter_config")
    oauth = OAuth1(config["consumer_key"],
               config["consumer_secret"],
               config["access_token"],
               config["access_token_secret"])

    # define screen names for candidates
    candidates = {'clinton' : 'hillaryclinton',
                  'trump' : 'realdonaldtrump',
                  'rubio' : 'marcorubio',
                  'sanders' : 'berniesanders',
                  'cruz' : 'tedcruz'}

    # define mongodb parameters
    coll_dict = {'trump': db.trump,
                 'clinton' : db.clinton,
                 'sanders' : db.sanders,
                 'cruz' : db.cruz,
                 'rubio' : db.rubio}
    client = MongoClient()
    db = client.tweets

    # get tweets and insert into mongodb
    max_calls = 180
    max_tweets = 3500
    for cand in candidates:
        results = get_tweets(candidates[cand], since_id = None)
        into_mongo(coll_dict[cand], results)

if __name__ == '__main__':
    main()
