import sys

total = 16180000.0
moment = 2507900.0
n = 8
result = 0.0
j = 1

def cal(x, p):
    return ((x/2.0) * (1 + x/2.0) ** p)/((1 + x/2.0) ** p - 1)

def compare(x, p, t, m):
    y = cal(x, p) * t - m 
    return y

def interest(t, m, i, n):
    if n == 1 :
        return t - (m - t * i), t * i
    else :
        b, a = interest(t, m, i, n - 1)
        return b - (m - b * i), b * i

for i in range(1, 16) :
    while True:
        if compare(result + (1/10.0) ** j, n, total, moment) < 0 :
            result = result + (1/10.0) ** j
        else :
            break
    j = j + 1
    
for i in range(1, n+1):
    a, b = interest(total, moment, result/2, i)
    print format(moment - b, '.2f') + ", " + format(b, '.2f')

print format(result/2 * 100, '.4f') + "%"
print format(result * 100/365, '.4f') + "%"

a = 10844563.31
b = a / (1 + (result / 365) * 46)

print a - b

