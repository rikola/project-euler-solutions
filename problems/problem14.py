
MAX = 1000000

def collatzSequence(n):
    value = n
    count = 0
    while value > 1:
        if value % 2 == 0:
            value = value / 2
        else:
            value = 3 * value + 1
        count += 1
    return count

startVal = 0
longest = 0
longest = collatzSequence(13)

for i in range(MAX):
    sequenceLength = collatzSequence(i)
    if sequenceLength > longest:
        longest = sequenceLength
        startVal = i


print("Longest sequence is " + str(startVal) + " with length: " + str(longest))
