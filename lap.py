def g(x):
    # Định nghĩa hàm g(x) của phương trình
    return (-x**3+3*x**2+24*x-5)/24

def lap(x, epsilon):
    # Tìm nghiệm gần đúng của phương trình
    y=0
    while abs(x - y) > epsilon:       
        y = x
        x = g(x)
        #print(x,y)
    return x

print(lap(-1.5,0.0128))