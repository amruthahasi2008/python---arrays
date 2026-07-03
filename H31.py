# BINARY STREAK TRACKER
# PART 1 
binary_scores = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print("Binary Array:", binary_scores)

# PART 2 
current_streak = 0
for score in binary_scores:
    if score == 1:
        current_streak = current_streak + 1
    else:
        current_streak = 0
 
    print("Score:", score, "Current Streak:", current_streak)

# PART 3

current_streak = 0
best_streak = 0
for score in binary_scores:
    if score == 1:
        current_streak = current_streak + 1
        best_streak = max(best_streak, current_streak)
    else:
        current_streak = 0
 
print("Best Streak", best_streak)

# PART 4 
num = [0, 1, 0, 3, 12, 0, 5]
print("Original Array:", num)
write_pointer = 0
for read_pointer in range(len(num)):
    if num[read_pointer] != 0:
        num[write_pointer] = num[read_pointer]
        write_pointer = write_pointer + 1

print("After Array", num)
 
# PART 5 
while write_pointer < len(num):
    num[write_pointer] = 0
    write_pointer = write_pointer + 1
 
print("Final Array", num)
 