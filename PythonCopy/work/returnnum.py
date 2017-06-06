def returnnum(num):
    num = num-1
    print(num)
    if(num==0):
        return 0
    else:
	returnnum(num)
	    
returnnum(15)
