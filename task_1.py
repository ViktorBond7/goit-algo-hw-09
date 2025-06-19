def find_coins_greedy(amount):
    result = {}
    
    for i in denominations:
        count = amount // i
        if count > 0:
            result[i] = count
            amount -= count * i

    return result   


if __name__ == "__main__":
   
   denominations = [50, 25, 10, 5, 2, 1]
   result = find_coins_greedy(113)

   print(result)
 

