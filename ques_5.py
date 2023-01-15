a = int(input("Enter the number : "))

num= count = 0

while a>0:
    num= a%10
    a = a//10
    count +=1

print(count)
