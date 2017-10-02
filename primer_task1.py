from sympy import *
x = Symbol('x')
f = Function('f')
f = sin(x**2)*x  #函数

# 返回func的i阶导数
def result(func, x, i):
    return diff(func,x,i)

derivative_result = result(f, x, 1)
# x=6时，一阶导数的值
derivative_result_x = derivative_result.evalf(subs={x:6})

print("sin(x**2)*x的一阶导数是：", derivative_result)
print("x=6时，sin(x**2)*x的一阶导数结果是：", derivative_result_x)

