import math
import matplotlib.pyplot as plt
import time

def prod(a):
    p = 1
    for x in a:
        p = p * x
    return p

def LPUD(max_num,max_sum,length,product):
    if max_sum < length or product == 0:
        return []
    if length == 0 or product == 1 or max_num == 1:
        return [[1]*length]
    if length == 1:
        return [[min(max_sum,product,max_num)]]
    sol = []
    for i in range(1,min(max_num,max_sum-length+1)+1):
        sol += [[i] + L for L in LPUD(i,max_sum-i,length-1,product//i)]
    return sol
    
def possible_pref(n):
    length = math.ceil(math.log2(n))
    product = n
    sol = []
    for x0 in range(1,(n+3)//2 + 1):
        for L in LPUD(x0,n + length + 2 + 2*x0, length, product//x0):
            sol.append([x0] + L)
    return sol

def all_ends(n):
    sol = []
    for L in possible_pref(n-1):
        a = prod(L)
        b = sum(L) + n - 2 - math.ceil(math.log2(n-1))
        if a == 1:
            if b == 0:
                sol.append([b//2] + L)  
        elif b % (a-1) == 0:
            x0 = b//(a-1)
            if x0 < L[0]:
                continue
            sol.append([x0] + L)
    return sol



def a(n):
    return len(all_ends(n))

def go(seconds):
    with open('counter.txt') as file:
        for line in file:
            x = int(line)
            break
    
    with open('tryfind1.txt','a') as file:
        start = time.time()
        while (time.time()-start) < seconds:
            file.write(str(x)+ '   ' + str(a(x)) + '\n')
            x+=1
            
    with open('counter.txt','w') as file:
        file.write(str(x))
            

def test(n):
    for L in all_ends(n):
        print('sol ',L,'+[1] * ',n - len(L), '    S = ',sum(L) + n - len(L),'P =  ', prod(L))
def test_numbers(n):
    for L in all_ends(n):
        p = prod(L)
        if p != 2*n:
            print(p)
      
def test_mul_30(N):
    for i in range(1,N):
        print('TESTING ',30*i)
        test(i*30)
        
def test_numbers_mul_30(N):
    for i in range(1,N):
        print('TESTING ', 30*i)
        test_numbers(i*30)

def plot_a(N):
    y = [a(i) for i in range(2,N)]
    plt.plot(y)
    plt.show()
    
def print_a(N):
    for i in range(2,N):
        print(i , a(i))
    
def plot_complexity(N):
    rep = 1
    x,y = ([],[])
    for i in range(2,N):
        x.append(i)
        start = time.time()
        for _ in range(rep):
            all_ends(i)
        y.append((time.time()-start)/rep)
    plt.plot(x,y)
    plt.show()