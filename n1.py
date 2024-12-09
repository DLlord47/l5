from random import randint
def turn(c, ch):
    print(f"Ход: {ch}.")
    return c - ch

n = randint(4,30)
t = True
while n > 1:
    print(f"В куче {n} камней.")
    if t:
        n = turn(n, int(input('Сделай ход: ')))
    else:
        n = turn(n, randint(1,3))
    t = not t
if n == 1:
    print('Победа!' if not t else 'Поражение.')
else:
    print('Победа!' if t else 'Поражение.')