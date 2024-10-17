# Objective: Scrap image(s) from a tweet, download it to local, and adding the credit to the image(s)' metadata 
# Version: 0.0.1

import asyncio
import argparse
import Twitter_Account
from twscrape import API, gather



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
        Twitter_Post_ID.append(int(Link.split("/")[-1]))

    photo_url = await Twitter_Scraper(Twitter_Post_ID)




async def Twitter_Scraper(Tweet_ID: list):
    api = API()
    await api.pool.add_account(Twitter_Account.username, Twitter_Account.password, Twitter_Account.email, Twitter_Account.email_password)
    await api.pool.login_all()
    

    media_url = []

    for tweet in Tweet_ID:
        response = await api.tweet_details(tweet)
        media_array = response.dict()["media"]["photos"]

    for photo_url in media_array:
        media_url.append(photo_url["url"])

    return media_url




async def Download_Images(url: list):




if __name__ == "__main__":
    asyncio.run(main())