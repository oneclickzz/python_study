# f = open('newfile.txt', 'w')
# f.close()


# f = open('c:/doit/newfile.txt', 'w')
# f.close()


# f = open('c:/doit/newfile.txt', 'w')
# for i in range(1,11):
#     data = f'{i}번째 출력입니다\n'
#     f.write(data)
# f.close()

# f = open("c:/doit/newfile.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# EOF == end of file == /0 == null
# f = open("c:/doit/newfile.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     # if not f.readable(): break
#     print(line, end='')
# f.close()


# f = open("c:/doit/newfile.txt", 'r')
# lines = f.readlines()
# # print(lines)

# for line in lines:
#     print(line, end='')

# f.close()

# f = open("c:/doit/newfile.txt", 'r')
# data = f.read()
# print(data)
# f.close()


# f = open("c:/doit/newfile2.txt", 'a')
# for i in range(11,20):
#     data = f'{i}번째 출력입니다\n'
#     f.write(data)
# f.close()


# f = open("c:/doit/newfile_2.txt", 'r')
# f.close()

try:
    with open("c:/doit/newfile_2.txt", 'w') as f:
        f.write("Life is too short, you need python")
        
    with open("c:/doit/newfile_2.txt", 'r') as f:
        print('with as문 open file', f.read())
except:
    print('error')



# file = open(path, 'r', encoding='utf-8')



