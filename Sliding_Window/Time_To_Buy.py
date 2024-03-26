def maxProfit(prices):
    buy=0
    max=0
    for i in range(len(prices)):
        if prices[buy]>prices[i]:
            buy=i
        if max<(prices[i]-prices[buy]):
            max = prices[i]-prices[buy]
    return max

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print("prices = [7,1,5,3,6,4]")
    print(maxProfit(prices))