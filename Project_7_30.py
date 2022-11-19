

def gameWindow():
    print(d['1']+"|"+d['2']+'|'+d['3'])
    print("--"+"-"+"--")
    print(d['4']+"|"+d['5']+"|"+d['6'])
    print("--"+"-"+"--")
    print(d['7']+"|"+d['8']+"|"+d['9'])
    
    



d={'1':" ",'2':" ",'3':" ",'4':" ",'5':" ",'6':" ",'7':" ",'8':" ",'9':" "}

ans=gameWindow()
print(ans)

count=1


while(count<=9):
    while(1):
        num=input("Enter X or O for the game=")
        if(num=="X" or num=="O"):
            sym=num
            break
        else:
            print("Invalid move entered")
            continue
    while(1):
        move=input("Enter number of the move for the game from 1 to 9")
        Flag=True
        for i in range(1,10):
            if(str(i)==move):
                Flag=False
        if(Flag==True):
            print("Invalid move number entered")
            continue
        else:
            d[move]=sym
            print(gameWindow())
        
            

    
    
    

    
