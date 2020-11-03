from collections import defaultdict 
MAX_CHARS = 256

h = input()                                          #input     
distinct_length = len(set([i for i in h]))           #lengthing all the disticnt characters in the input
    
currrent_length = defaultdict(lambda: 0)            #maintaing the current length and start
length = 0
start = 0
minimum_length = len(h)
    
for i in range(len(h)):                               #Finding the substring contating all the distinct characters
    currrent_length[h[i]] += 1
        
    if currrent_length[h[i]] == 1:                #Increasing the length when we see a disticnt character.
        length += 1
            
    if length == distinct_length:                         #Removing the repated charaters in the substring we found, from the start 
        while currrent_length[h[start]] > 1: 
            if currrent_length[h[start]] > 1: 
                currrent_length[h[start]] -= 1
                    
            start += 1                                 #and update the start index
                 
        substring_lenghth = i - start + 1                      #and update the substring size

        if minimum_length > substring_lenghth:                        #and check if this substring is the minimum substring or not.if not we will upate the minimum lenghth
            minimum_length = substring_lenghth 
           
        
        current_length = start
         
print(len(str(h[current_length: current_length + minimum_length])))
