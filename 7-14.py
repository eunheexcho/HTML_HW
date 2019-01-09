# random number
from random import randint
random_num_1 = randint(0, 9)
random_num_2 = randint(0, 9)

while True:
    if random_num_2 == random_num_1:
        random_num_2 = randint(0, 9)
    else:
        break
random_list = [random_num_1, random_num_2]

random_num_3 = randint (0, 9)
while True:
    if random_num_3 in random_list:
        random_num_3 = randint(0, 9)
    else:
        break

random_list = [random_num_1, random_num_2, random_num_3]
print(random_list) # 코드 완성 후 삭제
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

# my number
print("세 수를 하나씩 차례대로 입력하세요.")
my_num_1 = int(input("1번째 수를 입력하세요: "))
while True:
    if my_num_1 < 0 or my_num_1 > 10:
        print("법위를 벗어나는 수입니다. 다시 입력해주세요.")
        my_num_1 = int(input("1번째 수를 입력하세요: "))
    else:
        break

my_num_2 = int(input("2번째 수를 입력하세요: "))
if my_num_1 == my_num_2:
    print("중복되는 수입니다. 다시 입력해주세요.")
    my_num_2 = int(input("2번째 수를 입력하세요: "))
while True:
    if my_num_2 < 0 or my_num_2 > 10:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        my_num_2 = int(input("2번째 수를 입력하세요: "))
    else:
        break

my_num_3 = int(input("3번째 수를 입력하세요: "))
while True:
    if my_num_3 == my_num_1:
        print("중복되는 수입니다. 다시 입력해주세요.")
        my_num_3 = int(input("3번째 수를 입력하세요: "))
    elif my_num_3 == my_num_2:
        print("중복되는 수입니다. 다시 입력해주세요.")
        my_num_3 = int(input("3번째 수를 입력하세요: "))
    else:
        break
while True:
    if my_num_3 < 0 or my_num_3 > 10:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        my_num_3 = int(input("3번째 수를 입력하세요: "))
    else:
        break
my_list = [my_num_1, my_num_2, my_num_3]
print(my_list) # 코드 완성 후 삭제

# random_list & my_list 비교하기
# 숫자의 값과 위치가 모두 일치하면 S입니다.
# 숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.

x = 0
while x < 3:
    b_count = [1, 2, 3]
    if my_list[x] in random_list[x]:
        print("%sB" % (b_count))
    x = x + 1

x = 0
while x < 3:
    s_count = [1, 2, 3]
    if my_list[x] == random_list[x]:
        print("%sS" % (s_count[x]))
    x = x + 1
