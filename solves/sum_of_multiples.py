#https://www.codewars.com/kata/514b92a657cdc65150000006

def sum_of_multiples(limit, multiple):
    n = (limit - 1) // multiple
    return (n * (n + 1) // 2) * multiple

def solution(number):
    if number > 0:
        return sum_of_multiples(number,3)+sum_of_multiples(number,5)-sum_of_multiples(number,15)
    return 0