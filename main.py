import csv

def main(dna_database, dna_sequence):
    print(f"Input dna_database: {dna_database}")
    print(f"Input dna_sequence: {dna_sequence}")

    database = read(dna_database)
    dna = create_list(database, dna_sequence)

    found = False
    no_match = False
    output = "No match"

    for i in range(1, len(database)):
        for j in range(1, len(database[0])):
            if int(database[i][j]) != dna[j - 1]:
                no_match = True
                break
        if no_match:
            no_match = False
            continue
        if found:
            return "No match"
        found = True
        output = database[i][0]
    print(output)

def read(path):
    output = []
    with open(path, 'r') as ifs:
        reader = csv.reader(ifs)
        for line in reader:
            output.append(line)
    return output

def longest_consecutive_str(dna_sequence, target_sequence):
    count = 0
    max_count = 0
    i = 0
    found = False
    while i < len(dna_sequence) - len(target_sequence) + 1:
        if target_sequence == dna_sequence[i:i + len(target_sequence)]:
            count += 1
            i += len(target_sequence)
            found = True
        else:
            i += 1
            if found:
                if max_count < count:
                    max_count = count
                count = 0
                found = False
    if found and max_count < count:
        max_count = count
    return max_count

def create_list(database, dna_sequence):
    output = []
    for i in range(1, len(database[0])):
        output.append(longest_consecutive_str(dna_sequence, database[0][i]))
    return output

if __name__ == '__main__':
    dna_database = "test.csv"
    dna_sequence = "TATTATTATTATAACCCTGCGCGCGCGCGATCCAGCATTAGCTAGCATCAAGATGAGATGAGATGGAATTTCGAAATGAATGAATGAATGAATGAATGAATG"
    main(dna_database, dna_sequence)
