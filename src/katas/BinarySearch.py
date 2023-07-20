from math import floor


def binary_search(haystack: list[int], needle: int) -> bool:
    low = 0
    high = len(haystack)

    while low < high:
        mid = floor(low + (high - low) / 2)

        if haystack[mid] == needle:
            return True
        elif haystack[mid] > needle:
            high = mid
        else:
            low = mid + 1

    return False


assert binary_search([1, 2, 3, 4, 5], 5) == True
assert binary_search([1, 2, 3, 4, 5], 6) == False
