# #먼저 모듈을 가져와야 한다
#
# import random
# import makemodule
#
#
# random_integer = random.randint(1, 10)
# 10을포함한다
# print(random_integer)
#
# print(makemodule.my_number)

#실수만들기 random.random
# import random
# #
# # random_num = random.random()
# # print(random_num)
# # 곱해서 랜덤수를 만든다
#
# random_float = random.uniform(0, 10)
# print(random_float)


#동전 뒤집기

# import random
# random_heads_or_tails = (random.randint(0, 1 ))
# if random_heads_or_tails == 1:
#     print("heads")
# else :
#     print("tails")


# # 주이름 저장하기
# state = ["delaware", "korea", "dd"]
# import random
#
# # 변경하기
# state[1] = "china"
#
# #추가하기
# state.extend(["korea", "japan"])
#
# print(state)

# import random
#
# friend = ["tae" , "kim", "gun", "power"]
#
# print(random.choice(friend))
#
# who = random.randint(0,3)
# print(friend[who])

# 중첩리스트
# fruits = ["apple", "banana", "cherry"]
# vegetables = ["pumkin", "spinach"]
#
# dirty = [fruits, vegetables]
#
# print(dirty)
# print(dirty[0][2])

import random

prs = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer = random.randint(0, 2)

if prs == 0 and computer == 2:
    print("You won!")
elif prs == 2 and computer == 0:
    print("You lost!")
elif prs > computer:
    print("You won!")
elif prs == computer:
    print("Draw!")
else :
    print("You lost!")