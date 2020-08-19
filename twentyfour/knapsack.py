import numpy as np


def knapsack(weights, prices, capacity, index=0):
    if (capacity == 0) or (index == len(weights)):
        return 0
    left = 0
    if capacity >= weights[index]:
        left = prices[index] + knapsack(weights, prices, capacity - weights[index], index + 1)
    right = knapsack(weights, prices, capacity, index + 1)
    return max(left, right)


def knapsackDP(weights, prices, capacity, memory, index=0):
    if (capacity == 0) or (index == len(weights)):
        return 0
    if memory.get((capacity, index)):
        return memory.get((capacity, index))

    left = 0
    if capacity >= weights[index]:
        left = prices[index] + knapsackDP(weights, prices, capacity - weights[index], memory, index + 1)
    right = knapsackDP(weights, prices, capacity, memory, index + 1)
    res = max(left, right)
    memory[(capacity, index)] = res

    return res


p = list(np.random.randint(5, 20, 100))
w = list(np.random.randint(5, 20, 100))
print(knapsackDP(w, p, 200, {}))
