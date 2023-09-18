# 采用循环的方式求第N个斐波那契数
def fibonacci_loop(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


# 测试代码
n = 10
print("斐波那契数列的第", n, "个数是：", fibonacci_loop(n))



