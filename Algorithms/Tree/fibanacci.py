def fibanacci(i, n, result, pre):
    print(result)
    if i < n:
        result = result + pre
        pre = result - pre
        i += 1
        fibanacci(i, n, result, pre)


result = 1
pre = 0
i = 0
n = int(input())
print(0)
fibanacci(i, n, result, pre)
