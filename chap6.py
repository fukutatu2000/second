#1
x = "カミュ"
print(x[0])
print(x[1])
print(x[2])

#2
what = input("何を書いた？-")
who = input("誰に送った？-")
y = "私は昨日{}を書いて、{}に送った！".format(what, who)
print(y)

#3
a = "aldous Huxley was born in 1894.".capitalize()
print(a)

#4
b = "どこで？　だれが？　いつ？".split("　")
print(b)

#5
list = ["The", "fox", "jumped", "over", "the", "fence", "."]
c = " ".join(list[:6]) + list[6]
print(c)

#6
d = "A screaming comes across the sky.".replace("s", "$")
print(d)
#7
e = "Hemingway".index("m")
print(e)

#8
f = "本物の本とは、私達が\"読む\"ものではなく、私達を\"読ませる\"ものだ。"
print(f)

#9
z = " three"
z = z + z + z
g = z.strip()
print(g)

z = " three"
z = z * 3
h = z.strip()
print(h)


#10
string = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
s = string.split("、")
print(s[0])
#sentence = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
#slce = sentence[:10]
#print(slce)
