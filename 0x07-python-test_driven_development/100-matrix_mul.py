#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")

    l = len(m_a[0])
    for row in m_a:
        if IndexError:
                raise ValueError("m_a can't be empty")
        for i in row: 
            if IndexError:
                raise TypeError("m_a must be a list of lists")
            elif type(i) != int:
                raise TypeError("m_a should contain only integers or floats")
        if l != len(row):
            raise TypeError("each row of m_a must be of the same size")

    new_matrix = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            prod = 0
            for k in range(len(m_a[0])):
                if TypeError:
                    raise ValueError("m_a and m_b can't be multiplied")
                prod += m_a[i][k] * m_b[k][j]
            new_row.append(prod)
        new_matrix.append(new_row)
    return new_matrix
