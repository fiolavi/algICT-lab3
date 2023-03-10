import time
import os

t_start = time.perf_counter()
def memory_usage_psutil():
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

f = open("input.txt")
n, k = map(int, f.readline().strip().split())

a = []
for i in f:
    a.append(list(map(int, i.strip().split( ))))

for i in range(len(a)):
    a[i] = ((a[i][0]**2 + a[i][1]**2)**0.5, a[i])

def quick_sort(a):

    if len(a) <= 1:
        return a

    elem = a[0][0]

    left = []
    center = []
    right = []

    for x in range(len(a)):
        if a[x][0] < elem:
            left.append(a[x])
        elif a[x][0] == elem:
            center.append(a[x])
        else:
            right.append(a[x])

    return quick_sort(left) + center + quick_sort(right)

a = quick_sort(a)

for i in range(k):
    print(a[i][1])

print("Время:", time.perf_counter() - t_start)
print("Память:", memory_usage_psutil(), "мб")
f.close()
