#블랙잭 룰
#1.참가 여부 묻기, 이름 받기
#2. 카드 정보 입력
#3.룰 1. 22가 되면 패배 2. 최대 5장까지 받을 수 있음 3. A는 1또는 11로 사용, 4.QKN는 10으로 사용
#3. 5. A이외의 값이 11 이상이라면 자동으로 A를 1로 사용
#4, 첫장을 공개하고 그다음부터 더 받을지 그만 받을지 정할 수 있음
#5. 딜러도 같은 룰을 적용함, 15 이하의 경우 더 받게됨

import random
#카드 정보

trump = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
dealer = []
playerDeck = []
def playCardDraw():
    playerDeck.append(random.choice(trump))
    print(f"{player}様のカード\n{playerDeck}")

def dealCardDraw():
    dealer.append(random.choice(trump))
    print(dealer)

def cardCheck(player, cardList):
    cardSum = 0
    excard = cardList
    for card in cardList:
        if card == "A":
           cardList

            cardSum
    cardSum = sum(cardList)
    if cardSum > 21:
        print(f"{player}が負けました")
    elif cardSum == 21:
        print(f"BlackJack")

    return


#참가여부 묻기
player = input("名前を入力してください：").lower()

print(f"{player}様、ブラックザックゲームに参加してくれてありがとうございます。\nそれではゲームをはじめます。")


#list,append : 글자 하나를 넣음, list. extend : 단어 하나를 하나씩 끊어서 넣음
dealCardDraw()

playCardDraw()

ans = input("カードをもう一枚もらいますか？ ”Y” or ”N”で入力してください。")

if ans == "Y":
    playCardDraw()
    cardCheck(player, playerDeck)
