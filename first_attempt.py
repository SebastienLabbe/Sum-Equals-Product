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


def a(n):
    result = []
    gen_sol(1, [], result, n)
    return len(result)


for i in range(2, 40):
    print(a(i))
