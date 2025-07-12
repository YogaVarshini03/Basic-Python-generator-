def reverse_list(lst):
  for i in range(len(lst)-1,-1,-1):
    yield lst[i]
numbers=[1,2,3,4,5]
for num in reverse_list(numbers):
  print(num)
