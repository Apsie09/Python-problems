a = input()

# sum of only two digits ---->
# --------> sum = int((int(a) / 10) % 10) + int(a) % 10 


sum = 0
i = 0


for i in a:
    digit = int(i)
    sum = sum + digit
    
print(sum)