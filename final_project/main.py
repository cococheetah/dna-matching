import csv

def main(dna_database, dna_sequence):
    """
    Read a DNA database CSV file and a DNA sequence, then identify which individual
    in the database matches the DNA sequence based on longest consecutive STR counts.

    Args:
        dna_database: Path to the CSV file containing STR counts per individual.
        dna_sequence: The DNA sequence to analyze.
    """
    print(f"Input dna_database: {dna_database}")
    print(f"Input dna_sequence: {dna_sequence}")

    # Read the database into a list of rows
    database = read(dna_database)
    # Compute the longest run counts for each STR in the sequence
    dna = create_list(database, dna_sequence)

    found = False # Flag to indicate if a matching profile has been found
    no_match = False # Temporary flag to skip non-matching rows
    output = "No match" # Default output if no profile matches

    # Iterate over each individual (skip header row)
    for i in range(1, len(database)):
        # Compare each STR count for this individual
        for j in range(1, len(database[0])):
            # If any STR count differs, mark no_match and break
            if int(database[i][j]) != dna[j - 1]:
                no_match = True
                break
        if no_match:
            # Reset flag and continue to next individual
            no_match = False
            continue
        if found:
            # More than one match found => ambiguous, treat as no match
            return "No match"
        found = True
        # Record the matching individual's name
        output = database[i][0]
    # Print the result (either name or "No match")
    print(output)

def read(path):
    """
    Read a CSV file and return its contents as a list of rows.

    Args:
        path: Path to the CSV file.

    Returns:
        A list of rows, where each row is a list of string values.
    """
    output = []
    with open(path, 'r') as ifs:
        reader = csv.reader(ifs)
        for line in reader:
            output.append(line)
    return output

def longest_consecutive_str(dna_sequence, target_sequence):
    """
    Compute the maximum number of consecutive repeats of target_sequence in dna_sequence.

    Args:
        dna_sequence: The DNA sequence to search within.
        target_sequence: The STR pattern to look for.

    Returns:
        The longest run of consecutive repeats of target_sequence.
    """
    count = 0 # Current consecutive count
    max_count = 0 # Maximum consecutive count found
    i = 0 # Index pointer in dna_sequence
    found = False # Flag indicating if the last checked segment matched

    # Slide window through the dna_sequence
    while i < len(dna_sequence) - len(target_sequence) + 1:
        if target_sequence == dna_sequence[i:i + len(target_sequence)]:
            # Match found: increment count and advance by the length of the pattern
            count += 1
            i += len(target_sequence)
            found = True
        else:
            # No match: if we were in a matching run, update max_count
            i += 1
            if found:
                if max_count < count:
                    max_count = count
                count = 0
                found = False
    # Final check after loop ends
    if found and max_count < count:
        max_count = count
    return max_count

def create_list(database, dna_sequence):
    """
    Build a list of longest runs for each STR defined in the database header.

    Args:
        database: The DNA database as a list of rows (first row is header of STRs).
        dna_sequence: The DNA sequence to analyze.

    Returns:
        A list of integers representing the longest run count for each STR.
    """
    output = []
    # Iterate over each STR column in the header (skip the name column)
    for i in range(1, len(database[0])):
        # Compute longest run for this STR and append to output
        output.append(longest_consecutive_str(dna_sequence, database[0][i]))
    return output

if __name__ == '__main__':
    # Example usage (change as needed)
    dna_database = "test.csv"
    dna_sequence = "TATTATTATTATAACCCTGCGCGCGCGCGATCCAGCATTAGCTAGCATCAAGATGAGATGAGATGGAATTTCGAAATGAATGAATGAATGAATGAATGAATG"
    main(dna_database, dna_sequence)