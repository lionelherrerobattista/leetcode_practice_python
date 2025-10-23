import heapq
from typing import List
from collections import defaultdict

# check if can be improved
# TODO: create a count to track tweets in time
# TODO: improve use of lists to simplify code


class Twitter:

    def __init__(self):
        # heap for 10 most recent tweets, max heap
        self.users_tweets = {}  # key user id, value tweets heap
        self.users_followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.users_tweets.keys():
            tweets = self.users_tweets[userId]
            tweets.append(tweetId)

        else:
            tweets = []
            tweets.append(tweetId)
            self.users_tweets[userId] = tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heapq.heapify(feed)

        # load recent users tweets to feed
        if userId in self.users_tweets.keys():
            user_tweets = self.users_tweets[userId]
            for tweet in user_tweets:
                # max heap, to get most recent
                if -1 * tweet not in feed:
                    heapq.heappush(feed, -1 * tweet)

        # loads followers tweets
        if userId in self.users_followers.keys():
            followers = self.users_followers[userId]
            for follower in followers:
                followers_tweets = self.users_tweets[follower]
                for follower_tweet in followers_tweets:
                    # max heap, to get most recent
                    if -1 * follower_tweet not in feed:
                        heapq.heappush(feed, -1 * follower_tweet)

        user_feed = []
        count = 0

        while feed and count < 10:
            user_feed.append(-1 * heapq.heappop(feed))
            count += 1

        return user_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users_followers.keys():
            # append the followee
            followees = self.users_followers[followerId]

            if followeeId not in followees:
                followees.append(followeeId)
        elif followerId != followeeId:  # edge case, user follows itself
            # create the array to store followers
            followees = []
            followees.append(followeeId)
            self.users_followers[followerId] = followees

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users_followers.keys():
            # find index
            followees = self.users_followers[followerId]
            if followeeId in followees:
                index_to_remove = followees.index(followeeId)
                followees.pop(index_to_remove)
