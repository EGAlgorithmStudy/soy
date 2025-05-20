def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    deliv = 0
    pick = 0

    for i in range(n):
        deliv += deliveries[i]
        pick += pickups[i]

        while deliv > 0 or pick > 0:
            deliv -= cap
            pick -= cap
            answer += (n - i) * 2

    return answer