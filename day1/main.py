sonar_data = []
previous_sample = 9999
count = 0


def open_file(name):
    with open(name, 'r') as f:
        for sample in f:
            sample = int(sample.strip())
            sonar_data.append(sample)


# day 1 #
open_file('input.txt')

for current_sample in sonar_data:
    if current_sample > previous_sample:
        count += 1
    previous_sample = current_sample

print(f'A: count: {count}')

# day 2 #
count = 0
previous_sample = [9999, 9999, 9999]

for x in sonar_data:
    if sum([previous_sample[-2], previous_sample[-1], x]) > sum(previous_sample):
        count += 1
    previous_sample = [previous_sample[-2], previous_sample[-1], x]

print(f'B: count: {count}')
