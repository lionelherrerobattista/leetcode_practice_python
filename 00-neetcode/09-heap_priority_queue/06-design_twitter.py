import heapq
from typing import List
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.count = 0
        # userId -> list of [count, tweetIds]
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)  # userId -> set of followeeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        # save the time and id of tweet
        self.tweet_map[userId].append((self.count, tweetId))
        # modify time
        self.count -= 1  # negative, max heap

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        user_feed = []

        # also add his/her tweets
        self.follow_map[userId].add(userId)

        # loads followers tweets
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                # get last index of the list
                index = len(self.tweet_map[followeeId]) - 1
                count, tweet_id = self.tweet_map[followeeId][index]
                # to look for next position
                heapq.heappush(
                    min_heap, (count, tweet_id, followeeId, index - 1))

        while min_heap and len(user_feed) < 10:
            count, tweet_id, followeeId, index = heapq.heappop(min_heap)
            user_feed.append(tweet_id)

            if index >= 0:
                count, tweet_id = self.tweet_map[followeeId][index]
                heapq.heappush(
                    min_heap, (count, tweet_id, followeeId, index - 1))

        return user_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)  # add to the set

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)  # add to the set
