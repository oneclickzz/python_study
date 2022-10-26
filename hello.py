from ast import Try


print('Hello')

# while True:
#     print('Hello')
#     if exit:
#         break

integer = 10
double = 10.1123123123131312313123123131321323
integer2 = -10
double2 = -10.10

print("숫자 integer:", integer)
print("숫자 double:", double)
print("숫자 integer2:", integer2)
print("숫자 double2:", double2)


print("숫자 integer+integer2:", integer+integer2)
print("숫자 double+double2:", double+double2)

print("숫자 10**10:", 10 ** 10)
print("숫자 7 % 3:", 7 % 3)
print("숫자 7 // 4:", 7 // 4)


# 문자 == 단 하나의 문자만, 문자열 == 하나의 문자가 나열된거, 열은 다수, 순서를 가지고 있는 다수 
# "문자" '문자'   "'를 '문자'로 표시할때"   '"를 "문자"로 표시할때'

print("'문자열'")
print('"문자열"')

a = 'hello'
b = 'world'
print(a + b)

print("쌍따옴표를 표시하는 방법으로 \"서식문자\"")
print("줄내림 역시도 서식문자로\n표현이 가능합니다")

print('''
이렇게 줄내림을 해두면
명시적으로 우리 눈에서 이해가 쉽기에\n사용하면 가독성에 도움을 줄 수 있다
''')

print("="*50)
print("하나의문자열"*2)
print("="*50)

print("이 asdf문장의 길이는 몇일까? len:", len("이 asdf문장의 길이는 몇일까?"))

text = "문자열로써 인덱싱을 하는데 사용할 문자열"

# str = text[6:-5] + '추가된 글자'
# print("str: ", str)

format = "%10s" % "12345"
print("format:", format, sep="")

formatF = "%010.2f" % 3.14
print("formatF:", formatF, sep="")

print("1: 나의 이름은 {1}, {0} 입니다".format("이", "재권"))

print("2: 나의 이름은 {name}, {0} 입니다".format("이", name="재권"))

print("{0:#<10}끝".format("12345"))

print("{0:10.2f}끝".format(3.14))

print("{{}}".format())

name = "재권"
lastname = "이"

print(f'{name}, {lastname} {{}}')
print(f'{name:>10}')

print(f'{12345.14:010.5f}')

a = "aaabbbccc"
b = 'aaabbbccc'
c = str('aaabbbccc')

print("a의 개수: ", a.count('a'))
print("a의 개수: ", b.count('a'))
print("a의 개수: ", c.count('a'))

# print("b값의 인덱스: ", a.find('z'))

try:
    print("b값의 인덱스: ", a.index('z'))
except:
    print("오류:")

print("계속진행")

print("join: ", "#".join("asdf"))
print("join: ", "-".join(['010','9907','0317']))

print("upper: ", "a".upper())
print("lower: ", "B".lower())

# risekon@gmail.com
print("lower: ", "risekon@GMAIL.COM".lower())
print("lstrip:", "    risekon@GMAIL.COM".lower().lstrip(), sep="")
print("rstrip:", "risekon@GMAIL.COM    ".lower().rstrip() + "끝", sep="")
print("strip:", "    risekon@GMAIL.COM    ".lower().strip() + "끝", sep="")
print("replace:", "    risekon@GMAIL.COM    끝".replace(" ", ""), sep="")
print("replace:", "asdfasdf".replace("s", "w"), sep="")
print("replace:", "asdfasdf".replace("s", "w", 1), sep="")

print("join: ", "".join(["0","1","2"]))
print("split: ", "0,1,2".split(","))

split = "risekon@gmail.com".split("@")
id = split[0]
domain = split[1]

print("id:", id, sep="")
print("domain:", domain, sep="")
print("email:", "@".join([id, domain]) , sep="")



# print("type a: ", type(a))
# print("type b: ", type(b))
# print("type c: ", type(c))




