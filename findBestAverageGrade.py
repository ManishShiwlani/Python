import math


def maxAvgScore(scores):

    """variable to store the max value of an integer"""
    maxAvg = -math.inf
    """if scores is null then return 0"""
    if not scores: return 0
    """initialize an empty dictionary for grades"""
    grades = {}

    """for each name and score in scores tuple"""
    for name, score in scores:
        #if name is not in grades dictionary
        if name not in grades:
            #then set grades[name] to [0,0]
            grades[name] = [0, 0]
        # increment the score for name at first index
        grades[name][0] += int(score)
        # increment the name
        grades[name][1] += 1

    for val in grades.values():
        maxAvg = max(maxAvg, val[0] // val[1])

    return maxAvg

scores = [("Bob", "87"), ("Charles", "100"), ("Eric", "64"), ("Charles", "22")]


if __name__ == "__main__":
    print((maxAvgScore(scores)))

