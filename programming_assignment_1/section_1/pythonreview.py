import itertools

_arr = [1, 2, 3]
_val = 4


def findWithSum(arr, value, n=2):
    if n == 0 or len(arr) == 0:
        return {}

    new_arr = []

    for index, v in enumerate(arr):
        new_arr.append((index, v))

    res = {}

    for subsequences in itertools.combinations(new_arr, n):
        val = 0

        for tup in subsequences:
            val += tup[1]

        if val == value:
            for tup in subsequences:
                res[tup[0]] = tup[1]

    return res


if __name__ == '__main__':
    print(findWithSum(_arr, _val, 2))
