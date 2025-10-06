a = int(input('成绩1:'))
b = int(input('成绩2:'))
c = int(input('成绩3:'))

scorea = (60 <= a) * 1 + (90 <= a) * 2
scoreb = (60 <= b) * 1 + (90 <= b) * 2
scorec = (60 <= c) * 1 + (90 <= c) * 2
total = scorea + scoreb + scorec
print(total)
