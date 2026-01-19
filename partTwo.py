import math  

def main():
 A = int(input("what is side A?"))
 B = int(input("what is side B?"))
 pythag(A,B)

def pythag(A,B):
    n = ((A**2) + (B**2))
    print(n) #check is it times it correctly
    C = int(math.sqrt(n))
    print(C) #after it is square rooted

main()
