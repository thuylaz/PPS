def f(x):
    # Định nghĩa hàm f(x) của phương trình đa thức bậc n
    return x**4 - 2*x**3-4

def fdh(x):
    # Định nghĩa hàm f'(x)
    return 4*x**3 -6*x**2

def tieptuyen(a, b,epsilon): 
    x=b
    y=0
    while(abs(f(x)/fdh(x))>epsilon):
        y=x
        x=y-(f(y)/fdh(y))
    return x

print("Nghiệm gần đúng x =", tieptuyen(2, 3,0.01))