# Count solutions,
import math
def prod(a):
    p = 1
    for x in a:
        p = p * x
    return p

def gen_sol(k, attempt, result, n):

    if len(attempt) == n:
        if sum(attempt) == prod(attempt):
            result.append(attempt)

        return

    else:
        lower_bound = 1
        if len(attempt) != 0:
            lower_bound = attempt[-1]
            
        for i in range(lower_bound, 2*k+1):
            gen_sol(k+1, attempt + [i], result, n)
            
    return result




def gen_sol_mod(k, attempt, length, num_of_ones, n, result):
    
    if len(attempt) == length:
        if prod(attempt) - sum(attempt) == num_of_ones:
            result.append(attempt)
        return

    else:
        lower_bound = 1
        if len(attempt) != 0:
            lower_bound = attempt[-1]

        if k <= n - 1:
            for i in range(lower_bound, n - 1):
                gen_sol_mod(k+1, attempt + [i], length, num_of_ones, n, result)

        else:
            for i in range(lower_bound, 2*n + 1):
                gen_sol_mod(k+1, attempt + [i], length, num_of_ones, n, result)
    return result


def a_little_fast(n):
    num_of_ones = n - 1 - math.ceil(math.log(n, 2))
    k = num_of_ones + 1
    length = n - num_of_ones
    result = []
    gen_sol_mod(k, [], length, num_of_ones, n, result)
    return len(result)
    


for i in range(2, 30):
    print ("a({}) = {}".format(i, a_little_fast(i)))
    



