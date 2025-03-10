# dna-matching
BCOG 200 Final Project

This project will simulate a DNA profiling program that identifies individuals based on their unique Short Tandem Repeat (STR) patterns in a given DNA sequence. The program will read a DNA database file in CSV format, which contains individuals' names and the number of consecutive occurrences of specific STRs in their DNA. The program will analyze a provided DNA sequence to determine the longest consecutive occurrences of each STR and matches them to a person in the database. If an exact match is found, the program will output the individual's name; otherwise, it outputs "No match."

My project will have 3 functions excluding the Main function.
1. Read(): Reads a DNA database file and formats the data into a structured format that the program can manipulate, such as a list.
2. LongestConsecutiveSTR(): takes a DNA sequence and a target Short Tandem Repeat (STR) as inputs, then calculates the longest consecutive occurrence of the target STR, and returns the longest count as an integer.
3. CreateList(): Takes a DNA database and a DNA sequence, extracts STR counts from the sequence, and returns a list where each element represents the count of a specific STR.
