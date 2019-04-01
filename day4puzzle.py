import datetime
from collections import defaultdict

schedules = []
with open('guard_schedule.txt', 'r') as file:
    for line in file:
        schedules.append(line)

schedules.sort(key=lambda x: ''.join([x[6:8], x[9:11], x[12:14], x[15:17]]))

sleeptimes = {}
totalsleep = defaultdict(int)
for schedule in schedules:
    if 'begins shift' in schedule:
        guard = int(''.join(s for s in schedule[19:] if s.isdigit()))
        if guard not in sleeptimes:
            sleeptimes[guard] = defaultdict(int)

    if 'falls asleep' in schedule:
        start = datetime.datetime(year=int(schedule[1:5]), month=int(schedule[6:8]), day=int(schedule[9:11]),
                                  hour=int(schedule[12:14]), minute=int(schedule[15:17]))

    if 'wakes up' in schedule:
        end = datetime.datetime(year=int(schedule[1:5]), month=int(schedule[6:8]), day=int(schedule[9:11]),
                                hour=int(schedule[12:14]), minute=int(schedule[15:17]))
        for m in range(start.minute, end.minute):
            sleeptimes[guard][m] += 1

        totalsleep[guard] += end.minute - start.minute

sleepiest = 0
mostsleep = 0
for guard in totalsleep:
    if totalsleep[guard] > mostsleep:
        sleepiest = guard
        mostsleep = totalsleep[guard]

maxminute = 0
maxsleep = 0
for minute in sleeptimes[sleepiest]:
    if sleeptimes[sleepiest][minute] > maxsleep:
        maxminute = minute
        maxsleep = sleeptimes[sleepiest][minute]

print(sleepiest * maxminute)


consistentguard = 0
sleepiestminute = 0
minuteslept = 0
for guard in sleeptimes:
    for minute in sleeptimes[guard]:
        if sleeptimes[guard][minute] > minuteslept:
            minuteslept = sleeptimes[guard][minute]
            sleepiestminute = minute
            consistentguard = guard

print(consistentguard * sleepiestminute)