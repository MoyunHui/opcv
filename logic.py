import time

"""
print "road0 Car_num = 1"
time.sleep(1)
print "road0 Car_num = 2"
time.sleep(1)
print "road0 Car_num = 3"
time.sleep(1)
print "road0 Car_num = 4"
time.sleep(1)
print "road0 Car_num = 5"
time.sleep(1)
print "road0 Car_num = 6"
time.sleep(1)
print "road0 Car_num = 7"
time.sleep(1)
print "road0 Car_num = 8"
time.sleep(1)

print "road1 Car_num = 1"
time.sleep(1)
print "road1 Car_num = 2"
time.sleep(1)
print "road1 Car_num = 3"
time.sleep(1)
print "road1 Car_num = 4"
time.sleep(1)
print "road1 Car_num = 5"
time.sleep(1)


print "road2 Car_num = 1"
time.sleep(1)
print "road2 Car_num = 2"
time.sleep(1)
print "road2 Car_num = 3"
time.sleep(1)
print "road2 Car_num = 4"
time.sleep(1)

print "road3 Car_num = 1"
time.sleep(1)
print "road3 Car_num = 2"
time.sleep(1)
print "road3 Car_num = 3"
"""

road0_time, road1_time, road2_time, road3_time = [22, 22, 22, 22]

road0_num = 8
road1_num = 5
road2_num = 4
road3_num = 3
ave0 = 14*road0_num/road0_time
ave1 = 14*road1_num/road1_time
ave2 = 14*road2_num/road2_time
ave3 = 14*road3_num/road3_time
print "ave = ", ave0, ave1, ave2, ave3

diff = int((ave0+ave1) - (ave2+ave3))
if abs(diff) >= 1:
    road0_time = road0_time + diff
    road1_time = road1_time + diff
    road2_time = road2_time - diff
    road3_time = road3_time - diff

diff = int((ave0-ave1))
if abs(diff) >= 1:
    road0_time = road0_time + diff
    road1_time = road1_time - diff

diff = int((ave2-ave3))
if abs(diff) >= 1:
    road2_time = road2_time + diff
    road3_time = road3_time - diff
print "time_set = ", "%d, %d, %d, %d" % (road0_time, road1_time, road2_time, road3_time)
