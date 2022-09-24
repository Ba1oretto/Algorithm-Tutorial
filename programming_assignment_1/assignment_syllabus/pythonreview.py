import itertools


def findWithSum(arr, value, n=2):
    # if n is 0 or list is empty, should return empty dict.
    if n == 0 or len(arr) == 0:
        return {}

    new_arr = []

    # reformat value structure
    for index, v in enumerate(arr):
        new_arr.append((index, v))

    res = {}

    # looping subsequences from new_arr
    for subsequences in itertools.combinations(new_arr, n):
        val = 0

        # calculate value
        for tup in subsequences:
            val += tup[1]

        if val == value:
            # fill dictionary
            for tup in subsequences:
                res.__setitem__(tup[0], tup[1])

    return res
