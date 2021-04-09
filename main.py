import math
import concurrent.futures
import datetime

def x2(a, b, c, x):
    return round(a * x * x + b * x + c, 2)

def calculate(formula, abc_list):
    try:
        all_true = True
        for abc in abc_list:
            a, b, c = abc[0], abc[1], abc[2]
            X = round(eval(formula, globals(), locals()))
            Y = x2(a, b, c, X)
            all_true = Y == 0
            
            if not all_true:
                break
        return all_true
    except:
        return None


def plus(lev, lev_lim):
    if lev == lev_lim: 
        for a in chisla:
            for b in chisla:
                yield f'{a}+{b}'
    else:
        for a in generator(lev, lev_lim):
            for b in generator(lev, lev_lim):
                yield  f'({a})+({b})'

def minus(lev, lev_lim):
    if lev == lev_lim: 
        for a in chisla:
            for b in chisla:
                yield f'{a}-{b}'
    else: 
        for a in generator(lev, lev_lim):
            for b in generator(lev, lev_lim):
                yield  f'({a})-({b})'

def umnozit(lev, lev_lim):
    if lev == lev_lim: 
        for a in chisla:
            for b in chisla:
                yield f'{a}*{b}'
    else: 
        for a in generator(lev, lev_lim):
            for b in generator(lev, lev_lim):
                yield  f'({a})*({b})'

def delit(lev, lev_lim):
    if lev == lev_lim: 
        for a in chisla:
            for b in chisla:
                if b != 0:
                    yield f'{a}/{b}'
    else: 
        for a in generator(lev, lev_lim):
            for b in generator(lev, lev_lim):
                if b != 0:
                    yield  f'({a})/({b})'

def mypow(lev, lev_lim):
    if lev == lev_lim: 
        for a in chisla:
            for b in stepeni:
                if not(a == 0 and b < 0):
                    yield f'math.pow({a},{b})'
    else:
        for a in generator(lev, lev_lim):
            for b in stepeni:
                if not(a == 0 and b < 0):
                    yield f'math.pow({a},{b})'


# stepeni = [2, 3, -2, -3]
stepeni = [0.5]
operators = [plus, minus, umnozit, delit, mypow]
chisla = ['a', 'b', 'c', '0.0f', '1.0f']


def generator(lev, lim_lev):
    for op in operators:
        for formula in op(lev+1, lim_lev):
            yield formula
        


if __name__ == "__main__":
    minute = datetime.datetime.now().minute
    abc_array = [
        
        [1,     -1,     -2],
        [-1,    1,      6],
        [1,     0,      0],
        [1,     0,      -1],
        [2,     -2,     -8],
    ]
    lim = 1
    ret = False
    while(not ret):
        print(lim)
        for formula in generator(0, lim):
            new_minute = datetime.datetime.now().minute
            if new_minute != minute:
                minute = new_minute
                print(formula)
            if calculate(formula, abc_array):
                ret = True
                print(formula)
                break
        lim += 1
    print('Done')
       