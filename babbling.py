#programmers

from itertools import permutations

def solution(babbling):
    result = 0
    words = []
    # 아기가 말할 수 있는 어절들
    dict = ["aya", "ye", "woo", "ma"]
    for i in range(1, len(dict) + 1):
        for j in permutations(dict, i):
            words.append("".join(j))
    for k in babbling:
        if k in words:
            result += 1
    print(result)
    print(words)

solution(babbling=input())