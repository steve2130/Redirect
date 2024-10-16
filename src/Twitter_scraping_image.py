# Objective: Scrap image(s) from a tweet, download it to local, and adding the credit to the image(s)' metadata 
# Version: 0.0.1

import asyncio
import argparse
from twscrape import API,gather

class AsyncIterator:
    def __init__(self):
        self = self
    
    def __aiter__(self):
        return self




async def main():



    # Get url of the twitter post via console
    # Something like this: 
    #    PS C:\Users\Steve\Documents\GitHub\Redirect\src> python Twitter_scraping_image.py Hello
    #    ['Hello']

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url to the Twitter post", type=str, nargs="+")
    args = parser.parse_args()
    
    # Get the actual argc from console input
    Twitter_Post_Link = []
    Twitter_Post_ID = []

    for Link in args.url:
        Twitter_Post_Link.append(str(Link))
        Twitter_Post_ID.append(str(Link.split("/")[-1]))

    Tweet_ID = await Twitter_Scraper(Twitter_Post_ID)

async def Twitter_Scraper(Tweet_ID: list):
    api = API()

    async for rep in api.tweet_details_raw(Tweet_ID):
        print(rep.json())


if __name__ == "__main__":
    asyncio.run(main())