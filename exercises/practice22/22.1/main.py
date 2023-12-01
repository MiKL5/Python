numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]
totals = map(sum, numbers)
print(next(totals))  # 82
print(next(totals))  # 1186