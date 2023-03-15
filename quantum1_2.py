# -*- coding: utf-8 -*-
"""Quantum1_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-H1SszErF-wmdVS4EklzNrK0439p5uLR
"""

# Task 1
# You have a positive integer number N as an input. Please write a program in Python 3 that calculates the sum in range 1 and N.
# Limitations: N <= 10^25; Execution time: 0.1 seconds.

import time

# set limitations
MAX_EXECUTION_TIME = 0.1
MAX_N = 10**25

def calculate_sum(N):
    start_time = time.time()
    total_sum = N * (N+1) // 2
    end_time = time.time()
    execution_time = end_time - start_time
    if execution_time > MAX_EXECUTION_TIME:
        raise Exception("Execution time exceeded limit")
    if N > MAX_N:
        raise ValueError("Input value of N exceeds maximum limit")
    return total_sum
try:
    N = int(input("Enter the value of N: "))
    result = calculate_sum(N)
    print("Sum of numbers from 1 to", N, "is", result)
except ValueError as e:
    print("Invalid input value:", e)
except Exception as e:
    print("Error:", e)

# Task 2
# You have a matrix MxN that represents a map. 
# There are 2 possible states on the map: 1 - islands, 0 - ocean. 
# Your task is to calculate the number of islands in the most effective way. Please write code in Python 3.
# Inputs: M N, Matrix


def count_islands(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] != 1:
            return
        matrix[row][col] = -1
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                count += 1
                dfs(i, j)

    return count

import random

# Input the number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Generating a random matrix with values of 0s and 1s
matrix = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# Print the matrix
for row in matrix:
    print(row)
num_islands = count_islands(matrix)
print("The number of islands in the matrix is:", num_islands)