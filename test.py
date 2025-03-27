person_num = int(input())
i = 0
person_day = []
while i < person_num:
    person_day.append(input())
    i += 1
j = 0
count = 0
canday = []
k = 0
while k < 7:
    count = 0
    j = 0
    while j < person_num - 1:
        if person_day[j][k]=='1' and person_day[j+1][k]=='1':
            count += 1
        j += 1
    if count == person_num - 1:
        print(count)
        print(person_num)

        canday.append("가능")
    else:
        canday.append("불가능")
    k += 1

print("Sunday : " + canday[0] + 
      "\nMonday : " + canday[1] + 
      "\nTuesday : " + canday[2] + 
      "\nWednesday : " + canday[3] + 
      "\nThursday : " + canday[4] + 
      "\nFriday : " + canday[5] + 
      "\nSaturday : " + canday[6])