
limit = 1000

remainder = set()
sequenceLength = 0
num = 0

for i in range(limit, 1, -1):
    if sequenceLength >= i:
        break

    foundRemainders = [0] * i
    value = 1
    position = 0

    while foundRemainders[value] == 0 and value != 0:
        foundRemainders[value] = position
        value *= 10
        value %= i
        position += 1

    if position - foundRemainders[value] > sequenceLength:
        num = i
        sequenceLength = position - foundRemainders[value]

print(i, sequenceLength)
