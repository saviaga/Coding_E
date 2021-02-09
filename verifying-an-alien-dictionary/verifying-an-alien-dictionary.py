class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dic = {}
        for i in range(len(order)):
                order_dic[order[i]] = i
       
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            c=0
            while c <(len(min(word1,word2))):
               # print(word1[c],order_dic[word1[c]],"-",word2[c],order_dic[word2[c]])
                
                if word1[c]!=word2[c]: 
                    
                    #mean they are lexicograpphicaly ordered then no need to keep checking that word
                    if order_dic[word1[c]]<order_dic[word2[c]]:
                        break #with the word
                    elif order_dic[word1[c]]>order_dic[word2[c]]:
                            return False
                    
                # If we didn't find a first difference, 
                # words are like ("world", "word"). so that means that as first one is bigger is not in  lexicographical order 
                
                elif c==min(len(word1),len(word2))-1 and len(word1) > len(word2):
                        return False
                c+=1
                
        return True
            
                