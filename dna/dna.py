import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    database = []
    filepath = sys.argv[1]

    with open(filepath, 'r') as file:
        dataReader = csv.DictReader(file)
        for row in dataReader:
            database.append(row)


    # TODO: Read DNA sequence file into a variable
    filepathSequence = sys.argv[2]

    with open(filepathSequence, 'r') as file:
        sequenceReader = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    counts = {}
    subsequences = list(database[0].keys())[1:]
    print(subsequences)

    for i in subsequences:
        

        #l = {key: value for key, value in k.items() if key}
    """ agatcCount = longest_match(sequenceReader, "AGATC")
    aatgCount = longest_match(sequenceReader, "AATG")
    tatcCount = longest_match(sequenceReader, "TATC")


    counts.append(agatcCount)
    counts.append(aatgCount)
    counts.append(tatcCount) """

    #print(agatcCount, aatgCount, tatcCount)



    # TODO: Check database for matching profiles


    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
