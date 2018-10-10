with open("dataset.txt", 'w') as dataset_file:
    i = 1
    last = 2 * (10 ** 5)
    print(last, file=dataset_file)
    while i <= last:
        print(i, file=dataset_file, end=' ')
        i += 1
