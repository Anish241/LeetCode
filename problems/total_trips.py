class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        time.sort()
        low = 0
        high = sum(time) * totalTrips
        while low < high:
            mid = (low + high) // 2
            trips = 0
            for t in time:
                trips += mid // t
            if trips >= totalTrips:
                high = mid
            else:
                low = mid + 1
        return low
   
