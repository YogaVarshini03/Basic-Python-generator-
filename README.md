def num_generator(n):
    for i in range(1, n+1):
        yield i
for num in num_generator(5):
    print(num)
output:
1
2
3
4
5
