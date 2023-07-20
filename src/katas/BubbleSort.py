def bubble_sort(bundle: list[int]) -> list[int]:
    bundle_size = len(bundle)
    for i in range(bundle_size):
        for j in range(bundle_size - 1 - i):
            if bundle[j] > bundle[j + 1]:
                bundle[j], bundle[j + 1] = bundle[j + 1], bundle[j]

    return bundle


assert bubble_sort([2, 4, 3, 1]) == [1, 2, 3, 4]
