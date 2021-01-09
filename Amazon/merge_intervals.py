def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
            print("merged: ", merged)
            print("merged[-1][1]: ", merged[-1][1])
            print("interval 0: ", interval[0])
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            print("merged: ", merged)
            print("merged[-1][1]: ", merged[-1][1])
            print("interval 1: ", interval[1])

    return merged


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))