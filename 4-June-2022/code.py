import timeit
import numpy as np


def while_loop(n=100000000):
    sum = 0
    i = 0
    while i < n:
        sum += i
        i += 1
    return sum


def for_loop(n=100000000):
    sum = 0
    for i in range(n):
        sum += i
    return sum


def for_loop_with_increment(n=100000000):
    sum = 0
    for i in range(n):
        sum += i
        i += 1
    return sum


def for_loop_with_test(n=100000000):
    sum = 0
    for i in range(n):
        if i < n:
            pass
        sum += i
    return sum


def for_loop_with_increment_and_test(n=100000000):
    sum = 0
    for i in range(n):
        if i < n:
            pass
        sum += i
        i += 1
    return sum


def sum_range(n=100000000):
    return sum(range(n))

import numpy as np

def sum_numpy(n=100000000):
    return np.sum(np.arange(n))


def sum_formula(n=100000000):
    return (n * (n - 1)) // 2


import matplotlib.pyplot as plt

# Test each function 5 times
whileLoopTime                   = timeit.repeat(while_loop, number=1, repeat=5)
forLoopTime                     = timeit.repeat(for_loop, number=1, repeat=5)
forLoopWithIncrementTime        = timeit.repeat(for_loop_with_increment, number=1, repeat=5)
forLoopWithTestTime             = timeit.repeat(for_loop_with_test, number=1, repeat=5)
forLoopWithIncrementAndTestTime = timeit.repeat(for_loop_with_increment_and_test, number=1, repeat=5)
sumRangeTime                    = timeit.repeat(sum_range, number=1, repeat=5)
sumNumpyTime                    = timeit.repeat(sum_numpy, number=1, repeat=5)
sumFormulaTime                  = timeit.repeat(sum_formula, number=1, repeat=5)

# Print result
print(f'while loop                          {whileLoopTime}s')
print(f'for loop                            {forLoopTime}s')
print(f'for loop with increment             {forLoopWithIncrementTime}s')
print(f'for loop with test                  {forLoopWithTestTime}s')
print(f'for loop with increment and test    {forLoopWithIncrementAndTestTime}s')
print(f'sum range                           {sumRangeTime}s')
print(f'numpy sum                           {sumNumpyTime}s')
print(f'sum formula                         {sumFormulaTime}s')


plt.rcdefaults()
fig, ax = plt.subplots()

type = ('while loop',
        'for loop',
        'for loop with increment',
        'for loop with test',
        'for loop with increment and test',
        'sum range',
        'numpy sum',
        'sum formula')

y_pos = np.arange(len(type))

# Find mean
performance = []
performance.extend((np.mean(whileLoopTime),
                    np.mean(forLoopTime),
                    np.mean(forLoopWithIncrementTime),
                    np.mean(forLoopWithTestTime),
                    np.mean(forLoopWithIncrementAndTestTime),
                    np.mean(sumRangeTime),
                    np.mean(sumNumpyTime),
                    np.mean(sumFormulaTime)))

# Find error (standard deviation)
error = []
error.extend((np.std(whileLoopTime),
              np.std(forLoopTime),
              np.std(forLoopWithIncrementTime),
              np.std(forLoopWithTestTime),
              np.std(forLoopWithIncrementAndTestTime),
              np.std(sumRangeTime),
              np.std(sumNumpyTime),
              np.std(sumFormulaTime)))

# Construct horizontal bar chart
hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_title('Performance Comparison Between Each Method to Find a Sum of the First n Natural Numbers')
ax.set_xlabel('Time (s) - Lower is Better')
ax.set_xlim(right=7)
ax.set_yticks(y_pos, labels=type)
ax.invert_yaxis()

# Display label
for index, value in enumerate(performance):
    ax.text(value + 0.25, index - 0.125, f'{value}s', color='blue', va='center')
    ax.text(value + 0.25, index + 0.2, f'±{error[index]}s', color='red', va='center')

plt.show()