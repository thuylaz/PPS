
import numpy as np
from numpy.polynomial import Polynomial

def BTSP(arr_y, arr_x):
    result = [arr_y]
    for i in range(1, len(arr_y)):
        result.append([])
        for j in range(len(result[i-1])-1):
            m = (result[i-1][j+1] - result[i-1][j]) / (arr_x[j+i] - arr_x[j])
            result[i].append(m)
    return result

# #Newton tiến
def newton_up(arr_y, arr_x):
     arr_btsp = BTSP(arr_y, arr_x)
     #print(arr_btsp)
     result = [arr_y[0]]
     for i in range(1, len(arr_btsp)):
         f = [arr_btsp[i][0]]
         for j in range(0, i):
             f = np.convolve(f, [1, -arr_x[j]])
         result = np.polyadd(result, f)

     # Đảo ngược thứ tự của mảng hệ số
     result = np.flip(result)

     return result.tolist()

# Dữ liệu đầu vào
arr_x = [-2,-1,0,1]
arr_y = [-15,1,5,3]

# Kết quả
result = newton_up(arr_y, arr_x)
#result = newton_down(arr_y, arr_x)
print(Polynomial(result))



# #Newton lùi
# def newton_down(arr_y, arr_x):
#     arr_btsp = BTSP(arr_y, arr_x)
#     result = [arr_y[-1]]
#     for i in range(1, len(arr_btsp)):
#         f = [arr_btsp[i][-1]]
#         for j in range(0, i):
#             f = np.convolve(f, [1, -arr_x[-(j + 1)]])
#         result = np.polyadd(result, f)
#     result = np.flip(result)
#     return result.tolist()

    

# # Dữ liệu đầu vào
# arr_x = [10, 11, 12, 13]
# arr_y = [8.15, 8.34, 8.12, 8.25]

# # Kết quả
# #result = newton_up(arr_y, arr_x)
# result = newton_down(arr_y, arr_x)
# print(Polynomial(result))

