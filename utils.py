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

def convert(ls, reverse = False):
    '''
    Convert str list to integer list
    if reverse : convert integer list to integer list
    '''
    if reverse:
        return [str(x) for x in ls]
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
    splited = [l.split('-') for l in current_L]
    for fixed_value in splited: # fixed value
        for travel_value in splited: # traveling valuecla
            for tr in travel_value: 
                val = frozenset(fixed_value + [tr])
                if len(val) == level:  
                    res.add(val)
    # convert from set(frozenset,frozenset,...) to  [[],[],...]
    return list([list(convert(x,reverse=True)) for x in res]) 
    
def create_C(current_L,level,T):
    res =  create_c_keys(current_L,level,T)
    return count_values(res, T)

def createL(level, _set, epsilon = None):
    if level==1:
        return list(set(str(x) for l in _set for x in l))
    return [str(key) for key,value in _set.items() if value >= epsilon]

def create_result(C,eps):
    res = {}
    for c in C.values():
        for key,value in c.items():
            if value>=eps : res[key] = value
    
    return sorted(res.items(), 
                  key=lambda e: (e[1], len(e[0])), # sort by value then key length
                  reverse=True)
    
def dataset_from_file(input_file, delimeter):
    '''
    import dataset from external file
    '''
    res = []
    lines = open(input_file).read().splitlines()
    lines = [line.split(delimeter) for line in lines]
    for line in lines:
        res.append([word.strip() for word in line])
    return res

def format_output(res):
    print('{:15} {}'.format('element','value'))
    for elem in res: 
        print('{:17} {}'.format(elem[0],elem[1]))
        
def apriori(T,eps,verbose=False):
    '''
    main function
    '''
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
    return create_result(C,eps)
