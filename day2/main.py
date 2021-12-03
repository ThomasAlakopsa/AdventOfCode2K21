course = []
horizontal_pos = 0
depth = 0

def open_file(name):
    with open(name, 'r') as f:
        for sample in f:
            course.append(sample.strip())


open_file('input.txt')

for current_pos in course:
    if current_pos.split()[0] == 'up':
        depth -= int(current_pos.split()[1])
    elif current_pos.split()[0] == 'down':
        depth += int(current_pos.split()[1])
    else:
        horizontal_pos += int(current_pos.split()[1])

print(f'A: {horizontal_pos * depth}')

# B #
horizontal_pos = 0
depth = 0
aim = 0

for current_pos in course:
    if current_pos.split()[0] == 'up':
        aim -= int(current_pos.split()[1])
    elif current_pos.split()[0] == 'down':
        aim += int(current_pos.split()[1])
    else:
        horizontal_pos += int(current_pos.split()[1])
        depth += (aim * int(current_pos.split()[1]))

print(f'B: {horizontal_pos * depth}')