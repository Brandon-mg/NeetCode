import math


def minSpeed(piles, h):
    sort_piles = sorted(piles)
    if h == len(piles):
        return sort_piles[-1]
    min_speed = piles[-1]
    l=1
    r=piles[-1]
    while l<=r:
        mid = (r+l)//2
        total_time = 0
        for i in piles:
            total_time += math.ceil(float(i) / mid)
        if total_time<=h:
            min_speed = mid
            r=mid-1
        if total_time>h:
            l=mid+1
    return min_speed


if __name__ == "__main__":
    piles = [3,6,7,11]
    h=8
    print("piles = [3,6,7,11], h = 8")
    print(minSpeed(piles,h))