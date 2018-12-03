def remove_duplicates(numbers):
    sameNumbers = numbers[:]
    noDuplicates = []
    for digit in numbers:
        if digit not in noDuplicates:
            noDuplicates.append(digit)
        else:
            pass
    return noDuplicates

print(remove_duplicates([1, 2, 2, 3, 4, 6, 6, 6, 7, 8]))
            
        
