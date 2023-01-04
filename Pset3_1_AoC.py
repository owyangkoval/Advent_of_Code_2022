#rucksack reorganization part 1

def main():
    file = open('Pset3_1_AoC_input.txt', 'r')
    read = file.readlines()

    sum = 0
    for string in read:
        for val in priorities_list(string):
            sum += val
    print(f"Sum of Priorities = {sum}")

def priorities_list(string):

    # alphabet dict
    alpha_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
        'l': 12, 'm': 13,'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
        'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35,
        'J': 36, 'K': 37, 'L': 38, 'M': 39,'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47,
        'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

    # split string
    idx = None
    first_half = []
    second_half = []
    for idx in range(len(string)//2):
        first_half.append(string[idx])
    for idx in range(len(string)//2, len(string)):
        second_half.append(string[idx])

    # check item
    priority_list = []
    for letter_fh in first_half:
        for letter_sh in second_half:
            if letter_fh == letter_sh:
                key = letter_fh
                if key in alpha_dict and alpha_dict[key] not in priority_list:
                    priority_list.append(alpha_dict[key])
    return priority_list

if __name__ == '__main__':
    main()