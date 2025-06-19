def find_min_coins(amount, denominations = [50, 25, 10, 5, 2, 1]):
    # Ініціалізація: dp[i] — мінімальна кількість монет для суми i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # для суми 0 потрібно 0 монет

    # prev[i] — номінал останньої монети, який ми використали для формування суми i
    prev = [None] * (amount + 1)

    for coin in denominations:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                prev[x] = coin

    if dp[amount] == float('inf'):
        return {}  # неможливо здати решту

    # Відновлення словника номіналів
    result = {}
    while amount > 0:
        coin = prev[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


if __name__ == "__main__":
   result = find_min_coins(113)
   print(result)