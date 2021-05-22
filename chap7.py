list = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for title in list:
    print(title)

for i in range(25, 51):
    print(i)

for j, title in enumerate(list):
    j = str(j)
    print(j + ":" + title)

number = [0, 2, 9]
while True:
    a = input("type a number:")
    if a != "q":
        try:
            a = int(a)
            if a in number:
                print("正解")
            else:
                print("不正解")
        except ValueError:
            print("数字を入力するか、qで終了します")
    else:
        break


list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
multiplied = []
for i in list1:
    for j in list2:
        multiplied.append(i * j)
print(multiplied)
