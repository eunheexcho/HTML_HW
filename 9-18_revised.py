in_file = open("vocabulary.txt", "r")
voca_dict = {}
for line in in_file:
    eng_voca = (line.strip().split(": "))[0]
    kor_voca = (line.strip().split(": "))[1]
    voca_dict[kor_voca] = eng_voca
#print(voca_dict)

voca_keys = list(voca_dict.keys())
voca_values = list(voca_dict.values())
#print(voca_keys)
#print(voca_values)

while True:
    import random
    i = random.randint(0, len(voca_keys))
    quiz = input("%s: " % (voca_keys[i]))
    if quiz == "q":
        break
    if quiz == voca_values[i]:
        print("맞았습니다.")
    elif quiz != voca_values[i]:
        print("아쉽습니다. 정답은 %s입니다." % (voca_values[i]))