a = 1440

for i in range(2,100):
    if a%i==0:
        print(i)
        a = a//i
