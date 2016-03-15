__author__ = 'KG'
from datetime import datetime


junk = datetime.now().second
pick = "0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"[junk]
if datetime.now().second == 0:
    junk = datetime.now().minute * datetime.now().hour
else:
    junk = datetime.now().minute / datetime.now().second

if (len(str(junk)) > 8):
    junk *= len(str(junk)) + 1
elif (len(str(junk)) > 4):
    junk *= len(str(junk))
else:
    junk += len(str(junk))
print(str(junk) + pick)

junk = datetime.now().second * junk
if (len(str(junk))) > 8 and datetime.now().minute != 0:
    junk /= datetime.now().minute
sJunk = str(junk)
count = len(sJunk) - 1
picks = ""

while count >= 0:
    picks += sJunk[count]
    count -= 1

if picks[0] == "0":
    picks = "9876543219876543219876543219876543219876543219876543219876543219876543219876543219876543219876543219"[datetime.now().second] + picks
if len(picks) > 14:
    picks2 = picks[0]
    count = 14
    while count >= 1:
        picks2 += (str(count * datetime.now().second))[0]
        count -= 1
    count = 14
    while count < len(picks):
        picks2 += picks[count]
        count += 1
    print(picks2)
else:
    print(picks)
