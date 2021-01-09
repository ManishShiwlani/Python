

import heapq
class Solution:
    #     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    #         # The naive way is to first sort by start times and then add times
    #         # free rooms, allocating a new room if none are available
    #         # This requires for use to search for a free room at every iteration
    #         # which requires a lot of runtime. Instead we can use a min heap to
    #         # track the room that will get earliest free
    #         # then we are able to use the room if it's free, by replacing
    #         # or create a new room, by pushing
    #         # at the end, our heap size will be the number of rooms we require.

    #         min_heap = []

    #         intervals.sort()

    #         for start, end in intervals:
    #             if min_heap and start >= min_heap[0]:
    #                 heapq.heappop(min_heap)
    #             heapq.heappush(min_heap, end)

    #         return len(min_heap)

    def minMeetingRooms(self, intervals):
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        e = 0
        numRooms = available = 0
        for start in starts:
            while ends[e] <= start:
                available += 1
                e += 1
            if available:
                available -= 1
            else:
                numRooms += 1

        return numRooms

# def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#     if len(intervals) < 2:
#         return len(intervals)
#     intervals.sort(key = lambda x:x[0])
#     free_rooms = []
#     heapq.heappush(free_rooms, intervals[0][1])
#     for meeting in intervals[1:]:
#         if free_rooms[0] <= meeting[0]:
#             heapq.heappop(free_rooms)
#         heapq.heappush(free_rooms, meeting[1])
#     return len(free_rooms)


















#         # we need to find minimum number of groups of intervals
#         # such that the intervals in each group are not intersecting

#         # Naive: Start with 1 room and see if it's possible
#         # then try 2 rooms and all possible combinations and see if possible
#         # and so on

#         # Better: if we sort rooms by start time and then pick intervals
#         # 1 by 1, and only pick those intervals that don't intersect
#         # and then do that again once reaching end of array.
#         # this will obtain minimal number of groups because it will minimize
#         # the periods between the meetings for every group

#         res = 0
#         curr_end = 0

#         intervals.sort()

#         while intervals:
#             # will hold all the intervals to be considered for our current group
#             temp_intervals = []

#             for i in range(len(intervals)):
#                 # if interval fits into our current group, update end
#                 if intervals[i][0] >= curr_end:
#                     curr_end = intervals[i][1]
#                 else:
#                     # if it doesn't, add to group to be considered in next iteration
#                     temp_intervals.append(intervals[i])

#             intervals = temp_intervals[:]

#             # increment group number since we created 1 group in this iteration
#             res += 1

#             # reset group end
#             curr_end = 0

#         return res