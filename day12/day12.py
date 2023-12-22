
def compress(record_string: str):
    result_list = []
    for char in record_string.strip('.'):
        if char == '.' and result_list[-1] == '.':
            continue
        result_list.append(char)
    return "".join(result_list)

records = [(row[0], [int(item) for item in row[1].split(',')]) for row in (line.split() for line in open("day12/day12.txt"))]

def recursive_nonagram_row(record, notes):
    if ((len(notes) == 0 and (len(record) == 0 or '#' not in record))
        or (len(notes) == 1 and len(record) == notes[0] and '.' not in record)):
            return 1
    elif len(notes) == 0 or (len(notes) > 0 and len(record) == 0):
        return 0
    results = 0
    for index in range(len(record) - sum(notes[1:]) - len(notes[1:])):
        if (index+notes[0] <= len(record) and '.' not in record[index:index+notes[0]]) and (index+notes[0] == len(record) or record[index+notes[0]] != '#'):
            results += recursive_nonagram_row(compress(record[index+notes[0]+1:]), notes[1:])
        if record[index] == '#':
            break
    return results

result = 0
for record, notes in records:
    result += recursive_nonagram_row(compress(record), notes)
print(result)