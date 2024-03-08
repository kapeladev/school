
a = int(input("pjerwsza wartosc "))
b = int(input("druga wartosc "))
n = int(input("ile "))
p = [a , b]
print(p)
def f(x):
     return x*x+x+2   
x = (b - a ) / n 
s = 0 
mid = a+ (b-a) / (2.0*n)

for i in range(n):
    s += f(mid)
    mid +=  x

print(s*x)