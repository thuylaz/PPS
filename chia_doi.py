# def f(x):
#     # Định nghĩa hàm f(x) của phương trình đa thức bậc n
#     return 3*x**3 - x**2-1

# def chiadoi(a, b, epsilon):
#     # Sử dụng phương pháp chia đôi
#     while abs(b - a)/2 >= epsilon:       
#         c = (a + b) / 2
#         print(a,b,f(c))
#         if f(c) == 0:
#             return c
#         elif f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c      
#     return c

# print("Nghiệm gần đúng của phương trình là:", chiadoi(0, 1, 0.001)) 


def f(x):
    # Định nghĩa hàm f(x) của phương trình đa thức bậc n
    return 3*x**3 - x**2-1

def chiadoi(a, b, esp):
    c = (a + b) / 2
    count=0
    while (abs(b - a)/2 > esp and f(c)!=0 and count <=5):       
        print(a,b,f(c))
        count+=count
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c  
        c = (a + b) / 2
    return c

print("Nghiệm gần đúng của phương trình là:", chiadoi(0, 1, 0.001)) 