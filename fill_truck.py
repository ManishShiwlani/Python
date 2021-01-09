import heapq
from typing import List


def fill_truck(num: int, boxes: List[int], unitSize: int, unitsPerBox: List[int], truckSize: int) -> int:

    h = []
    fill, ans = 0, 0

    for i in range(len(unitsPerBox)):
        heapq.heappush(h, (-unitsPerBox[i], boxes[i]))

    while fill < truckSize and h:
        p = heapq.heappop(h)
        num_boxes = min(truckSize-fill, p[1])
        ans += -p[0] * num_boxes
        fill += p[1]
    return ans

num = 3
boxes = [1, 2, 3]
unitSize = 3
unitsPerBox = [3, 2, 1]
truckSize = 3
print(fill_truck(num, boxes, unitsPerBox, unitSize, truckSize))




