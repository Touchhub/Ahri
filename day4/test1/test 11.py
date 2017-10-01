# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(12))
def fib(max):
    n,a,b=0,0,1
    while n<max:
        #yield b
        a,b=b,a+b
        n+=1
    return (b)

def twice(n):
    n=int(n**2)
    return n
for i in range(1,21):
    a=(fib(i))
    b=(twice(i))
    print(a-b)