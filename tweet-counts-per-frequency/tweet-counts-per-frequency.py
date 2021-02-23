class TweetCounts:

    def __init__(self):
        self.dict_tweets = defaultdict(list)
        self.count=0

    def recordTweet(self, tweetName: str, time: int) -> None:        
            self.dict_tweets[tweetName].append(time)

            
            
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            seconds = 60
        
        if freq == 'hour':
            seconds = 3600
            
        if freq == 'day':
            seconds = 86400
        
        ordered_times = self.dict_tweets[tweetName]
        ordered_times.sort()
    #    print(ordered_times)
    #    print(startTime,endTime)

        ans = [0] * ((endTime - startTime)//seconds+1)
    #    print(ans)
        for t in self.dict_tweets[tweetName]:
     #       print(tweetName)
     #       print("dict",self.dict_tweets[tweetName])
            if startTime <= t <= endTime: ans[(t-startTime)//seconds] += 1
     #   print("ans",ans)
        return ans   
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)