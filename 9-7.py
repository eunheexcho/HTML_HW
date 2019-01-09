in_file = open("chicken.txt", "r")
sales_list = []
for line in in_file:
    arranged_file = line.strip()
    arranged_file = arranged_file.split(": ")
    #print(arranged_file) # 코드 완성 후 삭제

    sales = [int(arranged_file[1])]
    sales_list.append(sales[0])
#print(sales_list)
print(sum(sales_list) / len(sales_list))

in_file.close()

    #sales_list = [sales[0]]
    #i = 0
    #while i <= len(arranged_file):
        #sales_list = []            list가 for문의 영향을 받아 계속 loop처럼 돔. -> 빈 list는 for문 시작전에 만들어 놓을 것.
        #sales_list.append(sales)
        #i = i + 1
    #print(sales_list)