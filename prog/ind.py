#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_perimetr(func):
    def wrapper(*args, **kwars):
        return_value = func(*args, **kwars)
        print('Периметр фигуры равен', return_value)
    
    return wrapper


@print_perimetr
def periment(*args):
    values = [float(arg) for arg in args]
    P = 0
    
    for arg in values:
        P += arg
    return P


def main():
    periment(1, 2, 3, 4)


if __name__ == "__main__":
    main()