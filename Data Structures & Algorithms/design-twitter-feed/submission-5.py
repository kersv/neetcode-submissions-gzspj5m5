class Twitter:

    def __init__(self):
        self.followMap = collections.defaultdict(set)
        self.tweetMap = collections.defaultdict(list)

        self.timer = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        userList = []
        for follower in self.followMap[userId]:
            for tweet in self.tweetMap[follower]:
                userList.append(tweet)

        for tweet in self.tweetMap[userId]:
            userList.append(tweet)

        heapq.heapify(userList)

        while userList and len(res) < 10 :
            time, tweetId = heapq.heappop(userList)
            res.append(tweetId)
     
        
        return res
      
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].discard(followeeId)
        
