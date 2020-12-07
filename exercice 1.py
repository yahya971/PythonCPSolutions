def solution(n,a):
    maxi=0
    last_maxi=0
    last_op=0
    #resulting array
    ret=[0] * (n)
    #last update array to use max counter once for the entire array
    last_update=[0] * (n)
    
    for i in range(len(a)):
        #if max counter
        if(a[i]==n+1):
            last_maxi=maxi
            #we keep track of the time of last max_counter
            last_op=i

        # else if increase(x)
        else:
            idx=a[i]-1
            #if we have max counter that need to be done on a[idx] exclusively
            if(last_update[idx]<last_op):
                #we do increase(x) and max counter simultaneously
                ret[idx]=last_maxi+1
                #we keep track of this update so that we don't apply max counter next time on a[idx]
                last_update[idx]=i
            else:
                #we simply do increase(x)
                ret[idx]+=1
            #we update the max counter value
            maxi=max(maxi,ret[idx])
    
    # applying max counter to those that didn't have increase(x) operation
    for i in range(n):
        if(last_update[i]<last_op):
            last_update[i]=i
            ret[i]=last_maxi
    return ret

print(solution(5,[3,4,4,6,1,4,4]))



#the time and space complexity of this algorithm O(n) in worst case scenario