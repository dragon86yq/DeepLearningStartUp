from sympy import *
x = Symbol('x')
f = Function('f')
f = sin(x**2)*x

def result(func, x, i):
    return diff(func,x,i)

derivative_result = result(f, x, 1)
derivative_result_x = derivative_result.evalf(subs={x:6})

print(derivative_result)
print(derivative_result_x)

