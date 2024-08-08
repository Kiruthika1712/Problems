'''def pal(num):
    temp = 0 
    n = num
    while num>0:
        remainder = num%10 
        num = num//10 
        temp = temp*10+remainder
    
    if n==temp:
        print("Palindrome!")
    else:
        print("Not a Palindrome!")

pal(num = int(input()))'''

def pal(num):
    temp = 0 
    while num>0:
        remainder = num%10 
        num = num//10 
        temp = temp*10+remainder
    
    return temp

num = int(input())
print(num==pal(num))


        