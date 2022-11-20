# howManyGroups(n,m) = howManyGroups(n,m - 1) + howManyGroups(n - m,m)
def howManyGroups(n, m):
    # must return 1
    if n == 0:
        return 1
    # base Case
    if m == 0 or n < 0:  # for negative value
        return 0

    return howManyGroups(n, m - 1) + howManyGroups(n - m, m)

if __name__ == '__main__':
    print(howManyGroups(7, 3))
