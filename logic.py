
road0_time, road1_time, road2_time, road3_time = [25, 25, 19, 19]

road0_num = 10
road1_num = 7
road2_num = 7
road3_num = 4
ave0 = 10*road0_num/road0_time
ave1 = 10*road1_num/road1_time
ave2 = 10*road2_num/road2_time
ave3 = 10*road3_num/road3_time
print "ave = ", ave0, ave1, ave2, ave3

diff = int((ave0+ave1) - (ave2+ave3))
if abs(diff) >= 1:
    road0_time = road0_time + 2*diff
    road1_time = road1_time + 2*diff
    road2_time = road2_time - 2*diff
    road3_time = road3_time - 2*diff

diff = int((ave0-ave1))
if abs(diff) >= 1:
    road0_time = road0_time + 2*diff
    road1_time = road1_time - 2*diff

diff = int((ave2-ave3))
if abs(diff) >= 1:
    road2_time = road2_time + 2*diff
    road3_time = road3_time - 2*diff
print "%d, %d, %d, %d" % (road0_time, road1_time, road2_time, road3_time)
