
ALFA = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
        "j", "k", "l", "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "w", "x", "y", "z"]

ENCOD = ["ᔑ", "ʖ", "ᓵ", "↸", "ᒷ", "⎓", "⊣", "⍑", "╎",
         "⋮", "ꖌ", "ꖎ", "ᒲ", "リ", "𝙹", "!¡", "ᑑ", "∷",
         "ᓭ", "ℸ ̣",  "⚍", "∴", " ̇/", "||", "⨅"]


message = input("Type anything you want: ")
message = [*message]
count = 0
for j in message:
    print(f"=>>>>>{j}")
    count += 0
    while j != ALFA[count]:
        if count >= 25:
            count -= 1
            print("--=--", count)
        else:
            count += 1
            print("--_--", count)
    if j == ALFA[count]:
        print(j)


'''
for i in range(25):
    ALFA[i] = ENCOD[i]
    print(ALFA[i])

'''
