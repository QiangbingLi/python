import math
def y(x):
    return (x*x*x - x + 1)


def yprime(x):
    return (3*x*x-1)

x = 0.44
eta = 0.1
loop = 15
for i in range(loop):
    x = x - eta*yprime(x)
    print('%d: %6.3f, %6.3f' % (i, x, yprime(x)))
print('x_min = %6.3f' % (1/math.sqrt(3)))
print('y_min = %6.3f' % y(x))
