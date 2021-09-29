import os
import time

print(os.cpu_count())

start = time.perf_counter()

for number in range(1, 100):
  print("{} is {}".format(number, find_fibonacci(number)))

finish = time.perf_counter()

executed_time = round(finish - start, 2)
print(f"Finished in {executed_time} second(s)")
