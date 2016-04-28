import time
import itertools
start_time = time.time()

perms = list(itertools.permutations("0123456789"))

print(perms[999999])

print(time.time() - start_time)
