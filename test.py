from task_1 import find_coins_greedy 
from task_2 import find_min_coins 
import time

amount = 10000

start = time.time()
find_coins_greedy(amount)
print("Greedy час:", time.time() - start)

start = time.time()
find_min_coins(amount)
print("DP час:", time.time() - start)
