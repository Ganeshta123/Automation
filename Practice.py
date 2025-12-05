#factorial
fact= lambda n: 1 if n==0 else n*fact(n-1)
print(fact(5))