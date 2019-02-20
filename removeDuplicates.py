def withoutDuplicates(numbers):
    sameNumbers = numbers[:]
    noDuplicates = []
    for digit in sameNumbers:
        if digit not in noDuplicates:
            noDuplicates.append(digit)
        else:
            pass
    return noDuplicates

print(withoutDuplicates([1, 2, 2, 3, 4, 6, 6, 6, 7, 8]))



def remove_duplicates(numbers):
    sameNumbers = numbers[:]
    for digit in sameNumbers:
        if numbers.count(digit) == 1:
            continue
        else:
            numbers.remove(digit)
    return numbers

print(remove_duplicates([1, 2, 2, 3, 4, 6, 6, 6, 7, 8]))
        
