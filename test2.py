import time
import os

a = input("문자를 입력하세요 : ")

b = list(a)

while True:
    for i in range(0, len(b)-1):
        c = ''.join(b)
        print(c)
        b.insert(len(b)-i, b[len(b)-2-i])
        b.pop(len(b)-3-i)
        time.sleep(1)
        os.system('clear')        

# i=0
# while True:
#     i = i % (len(b)-1)
#     c = ''.join(b)
#     print(c)
#     b.insert(len(b)-i, b[len(b)-2-i])
#     b.pop(len(b)-3-i)
#     i+=1
#     time.sleep(1)
#     os.system('clear')
