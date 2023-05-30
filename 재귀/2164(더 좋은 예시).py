from collections import deque

def find_last_card(n):
    cards = deque(range(1, n+1))

    while len(cards) > 1:
        cards.popleft()  # 제일 위에 있는 카드를 버림
        top_card = cards.popleft()  # 제일 위에 있는 카드를 저장
        cards.append(top_card)  # 제일 아래로 옮김

    return cards[0]  # 마지막에 남은 카드 반환

n = int(input())
last_card = find_last_card(n)
print(last_card)
