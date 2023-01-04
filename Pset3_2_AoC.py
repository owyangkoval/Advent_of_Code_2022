# rucksack organization part 2

def main():
    file = open('Pset3_1_AoC_input.txt', 'r')
    read = file.readlines()

    priority_nums = []
    group_of_three = []
    for file_string in read:
        string = file_string.strip()
        if len(group_of_three) < 3:
            group_of_three.append(string)
        else:
            group_of_three = []
            group_of_three.append(string)
        if len(group_of_three) == 3:
            priority_num = list(priorities_list(group_of_three))[0]
            priority_nums.append(priority_num)

    sum = 0
    for val in priority_nums:
        sum += val
    print(f"Sum of Priorities in Groups of Three = {sum}")

def priorities_list(group_of_three):

    # alphabet dict
    alpha_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
        'l': 12, 'm': 13,'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
        'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35,
        'J': 36, 'K': 37, 'L': 38, 'M': 39,'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47,
        'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

    # check item
    priority_list = []
    setlist = []
    for val in group_of_three:
        letter_set = set(val)
        setlist.append(letter_set)
        common_letter = letter_set.intersection(*setlist)
    key = list(common_letter)[0]
    if key in alpha_dict:
        priority_list.append(alpha_dict[key])
    return priority_list


if __name__ == '__main__':
    main()