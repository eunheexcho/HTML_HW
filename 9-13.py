in_file = open("vocabulary.txt", "r")
eng_voca_list = []
kor_voca_list = []

for line in in_file:
    arr_file = line.strip().split(": ")
    # print(arr_file)

    eng_voca_list.append(arr_file[0])
    kor_voca_list.append(arr_file[1])
# print(eng_voca_list)
# print(kor_voca_list)

while True:
    import random
    i = random.randint(0, len(kor_voca_list))
    quiz = input("%s: " % (kor_voca_list[i]))
    if quiz == eng_voca_list[i]:
        print("맞았습니다.")
    else:
        print("아쉽습니다. 정답은 %s입니다." % (eng_voca_list[i]))

in_file.close()