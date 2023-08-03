# Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
# не превосходящие числа N.


userLimit = 10
i = 0
answer = 0
while answer < userLimit:
    answer = int(2**i)
    i += 1
    if answer > userLimit:
        break
    else:
        print(f"{answer}", end=', ')