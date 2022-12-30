#rucksack reorganization

def main():
    file = open('Pset3_1_AoC_input.txt', 'r')
    read = file.readlines()


def split_string(string):
    idx = 0
    first_half = []
    second_half = []
    if idx <= (len(string))//2:
        first_half.append(string[idx])
    if idx > (len(string))//2:
        second_half.append(string[idx])
    return first_half, second_half




if __name__ == '__main__':
    main()