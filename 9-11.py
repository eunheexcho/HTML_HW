eng_voca_list = []
kor_voca_list = []

while True:
    eng_voca = str(input("영어 단어를 입력하세요: "))
    if eng_voca == "q":
        break
    kor_voca = str(input("한국어 뜻을 입력하세요: "))
    if kor_voca == "q":
        break
    eng_voca_list.append(eng_voca)
    kor_voca_list.append(kor_voca)

#print(eng_voca_list)
#print(kor_voca_list)

out_file = open("vocabulary.txt", "w")
for i in range(len(eng_voca_list) - 1):
    out_file.write("%s: %s \n" % (eng_voca_list[i], kor_voca_list[i]))
out_file.close()