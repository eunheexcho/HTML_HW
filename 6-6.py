count = 1
chance = 4
from random import randint
random_num = randint(1,20)

while count <= 4:
    my_num = int(input("기회가 %d번 남았습니다. 1~20 사이의 숫자를 맞춰보세요: " % (chance)))
    chance = chance - 1
    if random_num == my_num:
        print("축하합니다. %d번만에 숫자를 맞췄습니다." % (count))
    elif random_num > my_num:
        print("Up")
    else:
        print('Down')
    count = count + 1

print("아쉽습니다. 정답은 %d였습니다." % (random_num))