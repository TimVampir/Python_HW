def nums_generator(n):
    for num in range(1, n + 1, 2):
        yield num


nums_gen = nums_generator(15)
print(nums_gen)
print(*nums_gen)
