def reverse_digit():
    n = int(input()) 
    ans = 0
    
    while n > 0:
        remainder = n % 10
        n = n // 10
        ans = ans * 10 + remainder
    return ans

print(reverse_digit())
