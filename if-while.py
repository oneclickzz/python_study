# if (조건이 참이라면) {
#     몸통의 로직을 처리
# }


import time
import os


money = 4000
health = 50

# if money >= 10000 or (health <= 50 and money >= 5000):
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")


if money >= 10000:
    print("택시를 타고 가라")
elif health <= 50:
    print("힘드니까 택시를 타고 가라")
else:
    print("걸어 가라")

# int result = 0;

# for (int i=0;i<3;i++) {
#     int n = arr[i]
#     if (n == 1) {
#         result = 1;
#         print("[1,2,3] 안에 1이 포함")
#         break;
#     }
# }

# if (result >= 1) {
#     print("[1,2,3] 안에 1이 포함")
# }

if 1 in [1,2,3]:
    print("[1,2,3] 안에 1이 포함")

if 4 not in [1,2,3]:
    print("[1,2,3] 안에 4가 미포함")

if '이재권' in '저는 대한민국에 사는 이재권입니다':
    print("이재권 포함")

# 기본구조
# while 조거문:
#     pass


treeHit = 0
while treeHit < 10: # 10미만일때만 몸통 처리
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다")
    # if treeHit == 10:
    #     print("나무 넘어갑니다.")

if treeHit >= 10:
    print("나무 넘어갑니다.")

os.system('cls')

prompt = "다음 행동을 선택해주세요(1-4): "
selection = '''
    1. Add
    2. Del
    3. List
    4. Quit
'''

number = 0
while number != 4:
    os.system('cls')
    print(selection)
    print(prompt)
    number = int(input())
    if number < 0 or number > 4:
        # break
        print("허용되지 않는 입력입니다")
        time.sleep(2)
        continue

print("종료되었습니다")