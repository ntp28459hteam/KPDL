import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f = open("agedetector_group_train.v1.0.txt", "r")
lines = []
line = f.readline()
while line:
    lines.append(line)
    line = f.readline()
    
datas = []
# group_18_24 = []
# group_25_34 = []
# group_35_44 = []
# group_45_54 = []
# group_55   = []
for line in lines:
#     print line
    label = line.split(" ", 1)[0][9:]
    label = label.replace("-", "_", 1)
    label = label.replace("+", "", 1)
    label = "group_" + label    
    # groups_str = lines[0].split(" ", 1)[1]
    groups_str = line.split(" ", 1)[1]
    groups_ = groups_str.split(" ")
    groups = [group.rstrip() for group in groups_]
    datas.append((label, groups))
    
group_list = {}
group_list['group_18_24'] = {}
group_list['group_25_34'] = {}
group_list['group_35_44'] = {}
group_list['group_45_54'] = {}
group_list['group_55'] = {}
for data in datas:
    label = data[0]
    for group in data[1]:
        if group not in group_list[label]:
            group_list[label][group] = 1
        else:
            group_list[label][group] += 1
# print group_list

x = []
y = []
i = -1
loop_range = range(0, 20, 1)
for i in loop_range:
    data = datas[i]
    label = data[0]
    i += 1
    for group in data[1]:
        x.append(i)
        y.append(group)
# plt.scatter(y[0], 'bo', label='visualization')
plt.plot(x, y, 'bo', ms = 1)
plt.show()
# print datas[2][1]
