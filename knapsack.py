def knapsack(value, weight, capacity):
    n = len(value) - 1
    m = [[-1]*(capacity + 1) for x in range(n + 1)]
    for w in range(capacity + 1):
        m[0][w] = 0
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weight[i] > w:
                m[i][w] = m[i - 1][w]
            else:
                m[i][w] = max(m[i - 1][w - weight[i]] + value[i], 
                              m[i - 1][w])
    return m[n][capacity]
 
 
n = int(input('Enter number of items: '))
value = input('Enter the values of the {} item(s) in order: '.format(n)).split()
value = [int(v) for v in value]
value.insert(0, None)
weight = input('Enter the positive weights of the {} item(s) in order: '.format(n)).split()
weight = [int(w) for w in weight]
weight.insert(0, None)
capacity = int(input('Enter maximum weight allowed in knapsack: '))
ans = knapsack(value, weight, capacity)
print('The maximum value of items that can be carried:', ans)
