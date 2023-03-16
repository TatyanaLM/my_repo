def count_unique_elements(lst):
    count = 0
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            count += 1
    return count

lst = [0, 9, 9, 45, 85, 89, 89, 90, 90, 789, 890]
print(count_unique_elements(lst))
