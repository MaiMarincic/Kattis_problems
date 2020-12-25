from itertools import product
varnames = {'p': 4,'q': 3,'r': 2,'s': 1,'t': 0}
def function(wff, vals):
    #Vraca v stilu (True/False, Se nepredelani podatki)
    if wff[0] in varnames:
        return vals[varnames[wff[0]]], wff[1:]
    elif wff[0] == 'N':
        ans, rem = function(wff[1:], vals)
        return not ans, rem
    elif wff[0] == 'K':
        a, second = function(wff[1:], vals)
        b, remain = function(second, vals)
        return a and b, remain
    elif wff[0] == 'A':
        a, second = function(wff[1:], vals)
        b, remain = function(second, vals)
        return a or b, remain
    elif wff[0] == 'C':
        a, second = function(wff[1:], vals)
        b, remain = function(second, vals)
        return (not a) or b, remain
    elif wff[0] == 'E':
        a, second = function(wff[1:], vals)
        b, remain = function(second, vals)
        return a == b, remain

while True:
    inp = input()
    if inp == '0':
        break
    _bool = True
    for combination in product([True, False], repeat=5):
        if function(inp, combination)[0] == False:
            _bool = False
            print('not')
            break
    if _bool:
        print("tautology")