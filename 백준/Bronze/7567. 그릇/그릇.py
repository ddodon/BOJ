plate = input()
length = 10
for i in range(1,len(plate)):
    if plate[i-1] + plate[i] == "((":
        length += 5
    elif plate[i-1] + plate[i] == "()":
        length += 10
    elif plate[i-1] + plate[i] == ")(":
        length += 10
    else:
        length += 5
print(length)