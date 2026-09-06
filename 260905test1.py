# / 나눗셈을 소수로 표현해주고 //는 정수 int로 표현해준다
# **는 거듭제곱이 된다
# round는 반올림 함수이다 round(반올림할수, 몇번째에서 반올림할지)
# f-String이라는 함수는 변수의 종류를 바꿔주는 함수로
# print(f'String = {다른 종류의 변수명}') 이걸 한번에 처리해준다

print("Welcome to the tip calculator!")


price = float(input("What was the total bill?"))

tipPercent = int(input("How much tip would you like to give?"))
person = int(input("How many people to split the bill?"))

totalPrice = ((price + (price * tipPercent)) / person)
print(f'Each person should pay : {totalPrice}')