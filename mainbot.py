import tweepy
import os # operating system library

def create_api():
  consumer_key = os.getenv('O4LSc7LXoA7EufH3m5YA05vL6')
  consumer_secret = os.getenv('AAAAAAAAAAAAAAAAAAAAAOpqHAEAAAAAjDi1Evm1VocDKu580dgGckhYE90%3DtZSYTOK2yGOEZVNtZSFJ0Wr5rhtRjZZmbi2F5gMHHN2fBZBwGP')
  access_token = os.getenv('1318019766-LLtfA9MI0xEdGKbp7dK80wr61grxuwxnrACPyQ6')
  access_token_secret = os.getenv('xJxvotMkCDjMJ5wqahKtFR25gNqWMpgIvZh8pbG4A1XKm')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]# Used to seperate 

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

while True:
    user = api.get_user('Bikramxx99')
    api.update_profile(name=f'Biktam|{follower_count(user)} Followers')
    print(f'Updating Twitter Name : Bikram|{follower_count(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
