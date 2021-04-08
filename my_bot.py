from instapy import InstaPy 

#headless_browser = True if you want to hide your browser
session = InstaPy(username = "", password = "", headless_browser = False)
session.login()

#You can set max and min followers here
session.set_relationship_bounds(enabled = True, max_followers = 500)

#Percentage from 0 to 100. 100 if you want to follow everyone who get your likes
session.set_do_follow(True, percentage=100)

#You will like posts with "bmw" and "steam" tags. If you set "amount = 3" 
#then you'll give 12 likes to "bmw" tag and 12 likes to "steam" tag
session.like_by_tags(["dog", "doglove"], amount = 3)
session.set_dont_like(["cat"])

# Unfollow users from your Following 
session.unfollow_users(amount=100, allFollowing=True, sleep_delay=60)

session.end()