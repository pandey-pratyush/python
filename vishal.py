user = input('Please Enter your name \n')
names = user.split()

for i in range(0, len(names)):
    if i < len(names) - 1:
        
        print(names[i][0], end=" ") 
    else:
        
        print(names[i])
