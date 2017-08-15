import cmath

# General tree implementation
class Tree(object):
    def __init__(self, id, children):
        self.id = id # col in current data file, attribute val for leaf (target attrbiute)
        self.children = children # dict: [val of attribute: Tree]

# Training phase methods: Construct decision tree
def column(data, i):
    return [row[i] for row in data]

def distinct_val(col):
    distinct = set(col)
    for val in distinct:
        dict[val] += 1
    return dict

def e(p):
    if p <= 0:
        return 0
    return -p*log(p)

def entropy(data, k):
    frequency = {} # dict = [attribute val : [target val : count]]
    distinct_attr = set(data[k])
    count_attr = distinct_val(data[k])
    n_attr = len(distinct_attr)
    distinct_target = set(data[-1])
    count_target = distinct_val(data[-1])
    n_target = len(distinct_target)
    for a in distinct_attr:
        for v in distinct_target:
            frequency[a][v] = 0
    for row in data:
        frequency[data[i]][data[-1]] += 1
    sum_e = 0
    for a in distinct_attr:
        p_a = count_attr[a]/n_attr
        e = 0
        for v in distinct_target:
            e += e(count_target[v]/n_target)
        sum_e += p_a * e
    return sum_e

def max_entropy_gain(data, visited): # On the same data set, sort by gain equivalent to sort by entropy
    max_e = 0
    max_i = 0
    for i in range(0, len(visited) - 1):
        if visited[i] == 1:
            continue
        e = entropy(data, i)
        if e > max_e:
            max_e = e
            max_i = i
    return max_i

def partition(data, visited):
    max_i = max_entropy_gain(data, visited)
    dict = distinct_val(column(data, max_i))
    dict_data = {} # dict [attribute val: paritioned data matrix]
    for val in dict.keys():
        for row in data:
            if val == row[max_i]:
                dict_data[val].append(row)
    return max_i, dict_data

def highest_freq(col):
    dict = distinct_val(col)
    max_key = 0
    max_val = 0
    for key in dict.keys():
        if dict[key] > max_val:
            max_key = key
            max_val = dict[key]
    return max_key

def leaf_case(dict_data):
    children = {}
    for key in dict_data.keys():
        data = dict_data[key]
        children[key] = highest_freq(column(data, -1))
    return children

def learn(data, visited):
    (id, dict_data) = partition(data, visited)
    visited[id] = 1
    for i in range(0, len(visited)):
        if visited[i] == 0 and i != len(visited) - 1:
            break
        else:# Leaf reached
            return Tree(id, leaf_case(dict_data))
    t = Tree(id, {})
    for val in dict_data.keys():
        t_child = learn(dict_data[val], visited)
        t.children[val] = t_child
    return t

def id3_train(data):
    visited = [0]*len(data[0])
    return learn(data, visited)

# Testing phase methods: Output learned results of testing data
def hypotehsis(row, dt):
    if not dt.children: # Leaf reached
        return dt.id
    return hypothesis(row, dt.children[row[dt.id]]) # Recursively going deeper

def id3_test(data, dt):
    for row in data:
        row.append(hypotehsis(row, dt))
    return data
