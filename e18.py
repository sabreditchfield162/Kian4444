jieguo = 0
for item in range(10, 51):
    unit =item %10
    if unit == 2 or unit==5 or unit==9:
        continue
    jieguo += item

print(jieguo)
