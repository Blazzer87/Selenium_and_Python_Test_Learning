N = int(input())

def get_sum(total):
    lst = []
    for i in range(1, total+1):
        lst.append(i)
        yield sum(lst)

x = get_sum(N)
lst = []
for i in x:
    lst.append(i)
str = " ".join(str(i) for i in lst)
print(str)


