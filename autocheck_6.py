from re import search
def fkkg(hello):
    re = r'\d+'
    k = True
    while k == True:
        finded = search(re, hello)
        yield finded.group()
        k = False


k = fkkg('106 money45 to  5m555y 7b78an9k:')
for i in k:
    print(i)

#sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000.")