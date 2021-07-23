#!/usr/bin/env python3
import os
from sql import db

cmd = 'system_profiler SPPowerDataType'
data = os.popen(cmd).read()
t = {
    "remain": 0, # 当前电量
    "capacity": 0, # 总电池容量
    "cycle_count": 0, # 电池循环次数
    "charging": False, # 是否在充电 
    "type": "real",
}

for line in data.splitlines():
    if 'Charge Remaining (mAh):' in line:
        t["remain"] = line.split()[-1]
    if 'Full Charge Capacity (mAh):' in line:
        t["capacity"] = line.split()[-1]
    if 'Cycle Count:' in line:
        t["cycle_count"] = line.split()[-1]
    if 'Charging:' in line:
        t["charging"] = True if line.split()[-1] != 'No' else False


db.insert_record(list(t.values()))