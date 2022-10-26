import time
import os

a = input("문자를 입력하세요 최대 9자: ")

b ="{0:#^9}".format(a)
b = b[0:9]

c = list(b)

while True:
    d = ''.join(c)
    print(d)
    c.extend(c[0])
    c.pop(0)
    time.sleep(1)
    os.system('clear')