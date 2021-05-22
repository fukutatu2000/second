tatsunori = {"height": 165,"fav_artist": "Aqours", "hobby": "female"}

def test():
    key = input("Type a key：")
    if key in tatsunori:
        value = tatsunori[key]
        print(value)
    else:
        print("見つかりません。")

test()
