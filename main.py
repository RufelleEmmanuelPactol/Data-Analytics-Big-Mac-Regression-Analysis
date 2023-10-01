# count subsequences

arr = [1, 6, 1, 7, 4, 2, 1]


def sum(array):
    total = 0
    for i in array:
        total += i
    return total


def subsequence(goal):
    count = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr) + 1):
            added = sum(arr[i:j])
            if added == goal:
                count += 1
            elif added > goal:
                break
    return count


print(subsequence(7))
