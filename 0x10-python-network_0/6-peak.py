#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(items):
    """Finds a peak in items"""

    if items is None or items == []:
        return None
    lo = 0
    hi = len(items)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)
    if hi == 1:
        return items[0]
    if hi == 2:
        return max(items)
    if items[mid] >= items[mid - 1] and\
            items[mid] >= items[mid + 1]:
        return items[mid]
    if mid > 0 and items[mid] < items[mid + 1]:
        return find_peak(items[mid:])
    if mid > 0 and items[mid] < items[mid - 1]:
        return find_peak(items[:mid])
