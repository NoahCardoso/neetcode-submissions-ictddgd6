class Twitter:

    def __init__(self):
        self.follows = dict()
        self.posts = dict()
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.posts.get(userId):
            self.posts[userId] = set()
        self.posts[userId].add((tweetId, self.count))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.posts)
        heap = []
        if not self.follows.get(userId):
            self.follows[userId] = set()
        self.follows[userId].add(userId)
        for user in self.follows[userId]:
            if self.posts.get(user):
                for post,rank in self.posts[user]:
                    heapq.heappush_max(heap,(rank,post))
        res = []
        print(heap)
        for i in range(10):
            if heap:
                _, post = heapq.heappop_max(heap)
                res.append(post)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.follows.get(followerId):
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.follows.get(followerId):
            self.follows[followerId].discard(followeeId)
