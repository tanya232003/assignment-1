a = int(input("enter first number : "))
b = int(input("enter second number : "))

if a<b:
    m=a
else:
    m=b

for i in range(2,m+1):
    if a%i == 0 and b%i == 0:
        gcf = i   

print(f"GCF if two number is {gcf}")

for i in range(2,m+1):
    if a%i == 0 and b%i == 0:
        lcm = i 
        print(f"LCF if two number is {lcm}") 
        break
