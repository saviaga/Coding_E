class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
        self.tweets[tweetName].sort()

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            seconds = 60
        
        if freq == 'hour':
            seconds = 3600
            
        if freq == 'day':
            seconds = 86400
       
        ans = [0] * (((endTime - startTime)//seconds)+1)
        
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime: 
                ans[(t-startTime)//seconds] += 1
        return ans         
        
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)