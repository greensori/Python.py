def kwardstest(**kwards):
    endtime = kwards.get('endtime', 1)
    starttime = kwards.get('starttime', 2)
    print ('start time %d, endtime %d' %(starttime, endtime))
    return
    

if __name__ == '__main__':
    kwardstest(endtime = 100)
    
    
## result : start time 100, endtime 2
