#Avarage of Student's Scores

scores =  {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, \
     "Tom" : 90, "Tim": 60}
avg = 0
count = 0
for i, j in scores.items():
    avg += j
    count += 1

print(f"{avg/count} is avarage of student's score")
