# BCOG 200 Final Project

This project simulates a **DNA profiling program** that identifies individuals based on unique Short Tandem Repeat (STR) patterns found within a given DNA sequence.

## Project Overview
The program reads a DNA database file in CSV format, which contains individuals' names and the number of consecutive occurrences of specific STRs in their DNA. The program analyzes a provided DNA sequence to determine the longest consecutive occurrences of each STR and matches them to a person in the database. If an exact match is found, the program will output the individual's name; otherwise, it outputs "No match."

## Functions
### `read(path)`
Reads a DNA database file and converts it into a list of lists.
- **Parameters**: `path (str)` - Filepath to the `.csv` file
- **Returns**: `List[List[str]]` - Nested list of rows

### `longest_consecutive_str(dna_sequence, target_sequence)`
Finds the longest consecutive repeat of a given STR in the DNA sequence.
- **Parameters**:
  - `dna_sequence (str)` - DNA sequence to analyze
  - `target_sequence (str)` - STR to search for
- **Returns**: `int` - Longest run of consecutive repeats

### `create_list(database, dna_sequence)`
Extracts STR counts from the sequence based on database headers.
- **Parameters**:
  - `database (List[List[str]])`
  - `dna_sequence (str)`
- **Returns**: `List[int]` - STR counts from sequence

### `main(dna_database, dna_sequence)`
Controls program flow: reads data, computes STR counts, and compares to the database.
- **Parameters**:
  - `dna_database (str)` - CSV filename
  - `dna_sequence (str)` - DNA string to analyze

## Data Input Format
The `.csv` file must be structured as follows:
- **First row**: column headers: `name`, followed by STRs
- **Subsequent rows**: individual's name, followed by STR counts

Example:
```csv
Names,AGATG,AATG,TAT
Elle,5,2,8
Amani,3,7,4
Blair,6,1,5
Ashley,3,7,1
```

## Example Use Case
Calling the `main()` function with a CSV file and DNA string:

```python
main("test.csv", "TATTATTATTATAACCCTGCGCGCGCGCGATCCAGCATTAGCTAGCATCAAGATGAGATGAGATGGAATTTCGAAATGAATGAATGAATGAATGAATGAATG")
```

### Output:
```
Input dna_database: test.csv
Input dna_sequence: TATTATTATTATAACCCTGCGCGCGCGCGATCCAGCATTAGCTAGCATCAAGATGAGATGAGATGGAATTTCGAAATGAATGAATGAATGAATGAATGAATG
Amani
```
