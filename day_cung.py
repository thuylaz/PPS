def f(x):
    # Định nghĩa hàm f(x) của phương trình
    return x**4 - 2*x**2

def daycung(a, b, epsilon):
    # Tìm nghiệm gần đúng của phương trình
    x = a - (b - a) * f(a) / (f(b) - f(a))
    if f(x) * f(a) < 0:
        while abs(x - b) > epsilon:
            b = x
            x = a - (b - a) * f(a) / (f(b) - f(a))
    else:
        while abs(x - a) > epsilon:
            a = x
            x = a - (b - a) * f(a) / (f(b) - f(a))
    return x

print("Nghiệm gần đúng:", daycung(-1.8, -1.2, 0.02)) 