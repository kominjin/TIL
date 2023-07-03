#별피라미드for문 
n=int(input('number:'))
for i in range(1,n+1):
    print(" "*(n-i),end="") #print(" "*(n-i),"*"*(2*i-1))이랑동일함
    print("*"*(2*i-1))
