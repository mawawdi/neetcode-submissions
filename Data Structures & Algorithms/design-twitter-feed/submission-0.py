class Twitter:

    # Map of users: key userId, value user's own deque(len=10) of postings
    # Map of followings: key userId which follows, value set of followingId(s)
    def __init__(self):
        self.t = 0
        self.users = {}
        self.relations = {}
        
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = deque(maxlen=10)
        self.users[userId].append((-self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if userId in self.users:
            for t in self.users[userId]:
                heap.append(t)
        if userId in self.relations:
            for f in self.relations[userId]:
                if f in self.users:
                    for t in self.users[f]:
                        heap.append(t)
        heapq.heapify(heap)
        res = []
        for _ in range(10):
            if not heap:
                break
            _, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.relations:
            self.relations[followerId] = set()
        self.relations[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.relations:
            return
        self.relations[followerId].discard(followeeId)
