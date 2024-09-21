import math

def f(x):
    return ((x-3)/(1+x))  # Hàm số mẫu, trong trường hợp này là e^x

def hinhthang(a, b, n):
    h = (b - a) / n  # Kích thước của mỗi hình thang
    integral = 0.5 * (f(a) + f(b))  # Tính giá trị ban đầu

    for i in range(1, n):
        x = a + i * h
        integral += f(x)  # Cộng thêm giá trị của mỗi hình thang

    integral *= h  # Nhân với kích thước hình thang

    return integral

print("Kết quả tích phân:", hinhthang(1,2,10))