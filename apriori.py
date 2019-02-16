
def _result(L,C):
    '''
    DEBUG purpose only
    '''
    for l_key, l_val in L.items():
        print('-'*10, end='')
        print('LEVEL {}'.format(l_key), end='')
        print('-'*10)
        print("l = {}".format(l_val))
        print('c = {}'.format(C[l_key]),end='\n\n')

def createKey(arr):
    '''
    Convert integer list to string
    Used to create the key in Cs results
    '''
    return '-'.join(str(x) for x in arr)

def _int(ls):
    '''
    convert list to int
    '''
    return [int(x) for x in ls]

def count_values(result,T):
    '''
    count values after creating 
    the corresponding L set
    '''
    final_res = {}
    for val in result:
        final_res[createKey(val)] = sum([set(val) <= set(t) for t in T])
    return final_res

def create_c_keys(current_L,level,T):
    res = set()
    int_l = [_int(l.split('-')) for l in current_L]
    for fixed_value in int_l: # fixed value
        for travel_value in int_l: # traveling value
            for tr in travel_value: 
                val = frozenset(fixed_value + [tr])
                if len(val) == level:  
                    res.add(val)
    # convert from set(frozenset,frozenset,...) to  [[],[],...]
    return list([list(x) for x in res]) 
    
def create_C(current_L,level,T):
    res =  create_c_keys(current_L,level,T)               
    return count_values(res, T)

def createL(level, _set, epsilon = None):
    if level==1:
        return list(set(str(x) for l in _set for x in l))
    return [str(key) for key,value in _set.items() if value >= epsilon]

def create_result(C):
    res = {}
    for c in C.values():
        for key,value in c.items():
            res[key] = value
    
    return dict(sorted(res.items(), 
                  key=lambda e: (e[1], len(e[0])), # sort by value then key length
                  reverse=True))
             
def apriori(T,eps, verbose = False):
    L,C = {},{}
    level = 1

    while True:
        L[level] = createL(
                level, T if level == 1 else C[level-1],eps)
        C[level] = create_C(L[level],level,T)
        if not C[level]: break # condition d'arret
        level += 1
    if verbose: 
        _result(L,C)
    return create_result(C)

res = apriori([[1, 2, 5], 
               [1, 3, 5],
               [2, 1], 
               [1, 2, 3, 4, 5], 
               [1, 2, 4, 5], 
               [2, 3, 5], 
               [1, 5]], 
            3)