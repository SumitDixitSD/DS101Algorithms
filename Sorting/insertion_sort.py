def insertion_sort(array):
  n = len(array)
  for index in range(1, n):
    key = array[index]
    position = index - 1
    while position >= 0 and array[position] > key:
      array[position + 1] = array[position]
      position = position - 1
    array[position + 1] = key
  return array

array = [8, 2, 4, 9, 3, 6]
print("Input array :", array)

result = insertion_sort(array)

print("Sorted list", result)
