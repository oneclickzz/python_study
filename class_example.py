
import math

result = 0

# def add(num):
#     global result
#     result += num

#     return result



class Calculator:
    lastName = "김"

    # name = '계산기'
    __privateAttr = '비공개:감춰짐'
    _protectedAttr = "보호된:"

    # def __init__(self):

    #     # print('init result: ', self.result)
    #     print('init name: ', self.name)

    #     self.result = 0
    #     # self.total = 1000
    #     # print('init total: ', self.total)
    #     pass

    def __init__(self, name="계산기"):
        self.name = name
        self.result = 0

    def nickname(self):
        return self.name + '-배가고픈자'
    
    def func1(self):

        self.total = 100

        print('func1 __privateAttr: ', self.__privateAttr)
        self.__privateFunc()
        pass

    def setPrivateAttr(self, attr):
        # 가공처리를 했어야합니다
        self.__privateAttr = "비공개:" + attr

    def __privateFunc(self):
        print('출력 __privateFunc::')
        pass

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        self.result /= num
        return self.result


class ExtendCalculator(Calculator):

    def pow(self, first, second):
        result = first ** second
        self.result = result
        return result

    def test(self):
        # print("__privateAttr: ", self.__privateAttr)
        print("_protectedAttr: ", self._protectedAttr)

    pass

class ExtendExtendCalculator(Calculator):
    pi = math.pi

    def __init__(self, name="계산기"):
        # super().__init__(name)
        Calculator.__init__(self, name)

        # print('super().name: ', super().name)

        # super().add(10000000000)
        # self.add(10000000000)

        pass

    def protectedTest(self):
        # print("__privateAttr: ", self.__privateAttr)
        print("_protectedAttr: ", self._protectedAttr)

        # super().add(10000000000)

    def setPrivateAttr(self, attr):
        print("setPrivateAttr: ")
        self.__privateAttrChild = "private:" + attr

        print("setPrivateAttr: self.__privateAttrChild: ", self.__privateAttrChild)
        # print("setPrivateAttr: super().__privateAttr: ", super().__privateAttr)

    def nickname(self):
        return self.name + '-진짜배고픈자'

    pass

# cal1 = Calculator()

# addResult = cal1.add(10)
# print(addResult)

# addResult = cal1.add(10)
# print(addResult)
# print("cal1.result: ", cal1.result)

# cal2 = Calculator()
# print("cal2.result: ", cal2.result)
# print("cal2.sub(100) : ", cal2.sub(100))


cal = Calculator()
cal.result = 100
# cal.result = cal.result + 100

print('cal.result: ', cal.result)
print('cal.name: ', cal.name)
print('cal.nickname(): ', cal.nickname())
# print('cal.private: '. cal.__privateAttr)
# print('cal.__privateFunc: '. cal.__privateFunc())
# print('cal.total1: ', cal.total) # 1000

cal.setPrivateAttr('바꼈음')
cal.func1()
# print('cal.total2: ', cal.total) # 100


calOther = Calculator("큰계산기")
print('calOther.name: ', calOther.name)
print('calOther.result: ', calOther.result)

extendCal = ExtendCalculator("확장된계산기")
print('extendCal.name: ', extendCal.name)
print('extendCal.nickname: ', extendCal.nickname())
extendCal.add(100)
extendCal.mul(100)
print('extendCal.result: ', extendCal.result)

extendCal.pow(10,10)
print('extendCal.result pow: ', extendCal.result)
extendCal.test()




extendExtendCal = ExtendExtendCalculator("다른확장계산기")
print('extendExtendCal.result pi: ', extendExtendCal.pi)
print('extendExtendCal.name: ', extendExtendCal.name)
print('extendExtendCal.nickname: ', extendExtendCal.nickname())
print('extendExtendCal.result: ', extendExtendCal.result)
extendExtendCal.protectedTest()
extendExtendCal.setPrivateAttr("접근제어")

print('extendExtendCal.protectedTest() -> result: ', extendExtendCal.result)


print("lastName: ", Calculator.lastName)
Calculator.lastName = "박"
print("lastName: ", Calculator.lastName)

calA = Calculator()
calB = Calculator()
print("calA.lastName: ", calA.lastName)
print("calB.lastName: ", calB.lastName)

Calculator.lastName = "최"
print("Calculator.lastName: ", Calculator.lastName)
print("calA.lastName: ", calA.lastName)
print("calB.lastName: ", calB.lastName)


calB.lastName = "이"

print("Calculator.lastName: ", Calculator.lastName)
print("calA.lastName: ", calA.lastName)
print("calB.lastName: ", calB.lastName)


class Person():
    def __init__(self, name) -> None:
        self.name = name

    def __eq__(self, __o: object) -> bool:

        hasName = hasattr(__o, 'name')
        print("hasName: ", hasName)

        if hasName:
            return __o.name == self.name

        return False

    def __str__(self) -> str:
        return "이 객제는 한 사람을 구성한것으로 그자의 이름은 " + self.name + " 이다"
    

class People():
    pass


person1 = Person("재권")
person2 = Person("재권")

people = People()

isEqual = person1 == person2
print('isEqual person1 == person2: ', isEqual)
print('isEqual person1 == people: ', person1 == people)
print('isEqual person1.name == people.name: ', person1.name == person2.name)

print("person1: ", person1)