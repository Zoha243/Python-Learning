# Print two pyramid in a single pattern
#*  
#* *  
#* * *  
#* * * *  
#* * * * *  
#* * * * * *  
#* * * * * * *  
#* * * * * * *  
#* * * * * *  
#* * * * *  
#* * * *  
#* * *  
#* *  
#*
for i in range(1,8):
    print(i*"*")
for i in range(8,1,-1):
    print(i*"*")
    
    