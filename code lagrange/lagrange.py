# import numpy as np
# from numpy.polynomial import Polynomial

# def lagrange_in(x, y):
#     n = len(x)
#     lagrange_poly = Polynomial([0.0])

#     for i in range(n):
#         v = Polynomial([1.0])
#         for j in range(n):
#             if i != j:
#                 poly_x_j = Polynomial([-x[j], 1.0])
#                 v *= poly_x_j / (x[i] - x[j])

#         lagrange_poly += y[i] * v

#     result_string = str(lagrange_poly)
#     print(result_string)

# # Nhập dữ liệu từ người dùng
# x_values = [-1, 0, 1, 2]
# y_values = [0.5, 1, 2, 4]

# # Gọi hàm và in kết quả
# lagrange_in(x_values, y_values)


import numpy as np
from numpy.polynomial import Polynomial

def lagrange_in(x,y):
    n=len(x)
    lp=Polynomial([0.0])

    for i in range(n):
        v=Polynomial([1.0])
        for j in range(n):
            if i!=j:
                poly_x_y=Polynomial([-x[j],1.0])
                v*=poly_x_y/(x[i]-x[j])
        lp+=y[i]*v
    result_string=str(lp)
    print(result_string)

x_value=[0,1,2,3]
y_value=[2,-1,0,3]

lagrange_in(x_value,y_value)

































