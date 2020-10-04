intervals = [[-100,-87],[-99,-44],[-98,-19],[-97,-33],[-96,-60],[-95,-17],[-94,-44],[-93,-9],[-92,-63],[-91,-76],
[-90,-44],[-89,-18],[-88,10],[-87,-39],[-86,7],[-85,-76],[-84,-51],[-83,-48],[-82,-36],[-81,-63],[-80,-71],[-79,-4],
[-78,-63],[-77,-14],[-76,-10],[-75,-36],[-74,31],[-73,11],[-72,-50],[-71,-30],[-70,33],[-69,-37],[-68,-50],[-67,6],
[-66,-50],[-65,-26],[-64,21],[-63,-8],[-62,23],[-61,-34],[-60,13],[-59,19],[-58,41],[-57,-15],[-56,35],[-55,-4],
[-54,-20],[-53,44],[-52,48],[-51,12],[-50,-43],[-49,10],[-48,-34],[-47,3],[-46,28],[-45,51],[-44,-14],[-43,59],[-42,-6],
[-41,-32],[-40,-12],[-39,33],[-38,17],[-37,-7],[-36,-29],[-35,24],[-34,49],[-33,-19],[-32,2],[-31,8],[-30,74],[-29,58],
[-28,13],[-27,-8],[-26,45],[-25,-5],[-24,45],[-23,19],[-22,9],[-21,54],[-20,1],[-19,81],[-18,17],[-17,-10],[-16,7],
[-15,86],[-14,-3],[-13,-3],[-12,45],[-11,93],[-10,84],[-9,20],[-8,3],[-7,81],[-6,52],[-5,67],[-4,18],[-3,40],
[-2,42],[-1,49],[0,7],[1,104],[2,79],[3,37],[4,47],[5,69],[6,89],[7,110],[8,108],[9,19],[10,25],[11,48],[12,63],
[13,94],[14,55],[15,119],[16,64],[17,122],[18,92],[19,37],[20,86],[21,84],[22,122],[23,37],[24,125],[25,99],[26,45],
[27,63],[28,40],[29,97],[30,78],[31,102],[32,120],[33,91],[34,107],[35,62],[36,137],[37,55],[38,115],[39,46],[40,136],
[41,78],[42,86],[43,106],[44,66],[45,141],[46,92],[47,132],[48,89],[49,61],[50,128],[51,155],[52,153],[53,78],[54,114],
[55,84],[56,151],[57,123],[58,69],[59,91],[60,89],[61,73],[62,81],[63,139],[64,108],[65,165],[66,92],[67,117],[68,140],
[69,109],[70,102],[71,171],[72,141],[73,117],[74,124],[75,171],[76,132],[77,142],[78,107],[79,132],[80,171],[81,104],
[82,160],[83,128],[84,137],[85,176],[86,188],[87,178],[88,117],[89,115],[90,140],[91,165],[92,133],[93,114],[94,125],
[95,135],[96,144],[97,114],[98,183],[99,157]]


# REMOVING MINIMUM NUMBER OF INTERVALS = KEEPING MAX INTERVALS = INTERVAL SCHEDULING PROBLEM = O(N)
print("Sorted by start,end\n")
print(sorted(intervals, key= lambda x: (x[0], x[1])));


print("\n")

print("Sorted by end")
print(sorted(intervals, key=lambda x: (x[1])))


def eraseOverlapIntervalscorrect(intervals):
        ans = list()
        
        # edge case:
        if not intervals: return 0
        
        # sort the given intervals according to (EndTime)
        intervals.sort(key=lambda interval: (interval[1]))
        
        # append the first one to ans since it is not overlapping.
        ans.append(intervals[0])
        
        for interval in intervals[1:]:
            start_time = interval[0]
            end_time = interval[1]
            
            # if starttime of new interval is less than endtime of previously added interval, skip that, else add that to ans since it is nonoverlapping.
            if start_time < ans[-1][1]:
                continue
            else:
                ans.append(interval)
        
        return ans

def eraseOverlapIntervalswrong(intervals):
        ans = list()
        
        # edge case:
        if not intervals: return 0
        
        # sort the given intervals according to (startTime, EndTime)
        # wrong because one long interval will mess up smaller intervals.
        # if for ex. next interval starts at 2--10, and gets selected, then 3-4, 4-5, 5-6 will not.
        intervals.sort(key=lambda interval: (interval[0], interval[1]))
        
        # append the first one to ans since it is not overlapping.
        ans.append(intervals[0])
        
        for interval in intervals[1:]:
            start_time = interval[0]
            end_time = interval[1]
            
            # if starttime of new interval is less than endtime of previously added interval, skip that, else add that to ans since it is nonoverlapping.
            if start_time < ans[-1][1]:
                continue
            else:
                ans.append(interval)
        
        return ans


print("\n\n Ans = wrong\n")
print(eraseOverlapIntervalswrong(intervals))

print("\n Ans = correct\n")
print(eraseOverlapIntervalscorrect(intervals))
