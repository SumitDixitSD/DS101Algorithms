def insertion_sort(a):
  n = len(a)
  for index in range(1, n):
    key = a[index]
    position = index - 1
    while position >= 0 and a[position] > key:
      a[position + 1] = a[position]
      position = position - 1
    a[position + 1] = key
  return a

a = [8, 2, 4, 9, 3, 6]
print("Input array :", a)

result = insertion_sort(a)

print("Sorted list", result)
