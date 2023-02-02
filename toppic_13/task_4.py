chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
original = {"1": ".,?!:",
            "2": "ABC",
            "3": "DEF",
            "4": "GHI",
            "5": "JKL",
            "6": "MNO",
            "7": "PQRS",
            "8": "TUV",
            "9": "WXYZ",
            "0": " ",
            }

"""
Написать в одну строку
"""
work = {}

for k, v in original.items():
    for idx, ch in enumerate(v, 1):
        work[ch] = str(k) * idx


for ch in input().upper():
    print(work.get(ch, ""), end="")
