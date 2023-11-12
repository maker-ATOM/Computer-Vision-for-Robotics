import numpy as np

a = np.array([[1], [0], [0]])
b = np.array([[0], [1], [0]])
c = np.array([[0], [0], [1]])
d = np.array([[1], [1], [1]])

# 2/3 = 0.66
# 1/3 = 0.33
# 5/3 =1.66

trans = np.array([[-0.66, 0, 1], [0, 1.66, -2], [0.33, -1.66, 1]])

ar = np.dot(trans, a)
br = np.dot(trans, b)
cr = np.dot(trans, c)
dr = np.dot(trans, d)

print(ar)
print(br)
print(cr)
print(dr)