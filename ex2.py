import time
import os

t_start = time.perf_counter()
def memory_usage_psutil():
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

f = open("input.txt")
n = int(f.readline())

x = 'x'
list = [x for i in range(n)]
pos = dict()
for i in range(n, 0, -1):
    element = i

    if element == 2:
        element = 1
    elif element == 1:
        element = 2

    if list[(i - 1) // 2] != x:
        list[pos[(i - 1) // 2]] = element
    else:
        list[(i - 1) // 2] = element

    if i - 1 in pos.keys():
        pos[(i - 1) // 2] = pos[i - 1]
    else:
        pos[(i - 1) // 2] = i - 1

mf = open("output.txt", "w+")
mf.write(' '.join(map(str, list)))
mf.close()

print("Время:", time.perf_counter() - t_start)
print("Память:", memory_usage_psutil(), "мб")
f.close()
