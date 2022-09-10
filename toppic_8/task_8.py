letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
c = ""
for i in letters:
    if not i.isupper():
        c += i
print(c)