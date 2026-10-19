def remove_negatives(data):
    return [[n for n in row if n >= 0] for row in data]

def square_elements(data):
    return [[n ** 2 for n in row] for row in data]

def sort_elements(data):
    return [sorted(row) for row in data]

def arrange_rows(data):
    return sorted(data, key=sum)

def tuple_conversion(data):
    return [tuple(row) for row in data]


matrix = [
    [5, -2, 8, 1],
    [-4, 7, 3, -1],
    [9, 2, -6, 4]
]

print("Original Matrix:")
print(matrix)

result1 = remove_negatives(matrix)
print("\nAfter Filtering Negative Values:")
print(result1)

result2 = square_elements(result1)
print("\nAfter Squaring Elements:")
print(result2)

result3 = sort_elements(result2)
print("\nRows Sorted in Ascending Order:")
print(result3)

result4 = arrange_rows(result3)
print("\nRows Sorted According to Their Sum:")
print(result4)

result5 = tuple_conversion(result4)
print("\nFinal Matrix as Tuples:")
print(result5)
