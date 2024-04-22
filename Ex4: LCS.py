def compute_lcs_length_and_direction(seq1, seq2):
    length_seq1 = len(seq1)
    length_seq2 = len(seq2)
    lcs_length_table = [[0] * (length_seq2 + 1) for _ in range(length_seq1 + 1)]
    direction_table = [[''] * (length_seq2 + 1) for _ in range(length_seq1 + 1)]

    for index_seq1 in range(1, length_seq1 + 1):
        for index_seq2 in range(1, length_seq2 + 1):
            if seq1[index_seq1 - 1] == seq2[index_seq2 - 1]:
                lcs_length_table[index_seq1][index_seq2] = lcs_length_table[index_seq1 - 1][index_seq2 - 1] + 1
                direction_table[index_seq1][index_seq2] = 'D'
            else:
                if lcs_length_table[index_seq1 - 1][index_seq2] >= lcs_length_table[index_seq1][index_seq2 - 1]:
                    lcs_length_table[index_seq1][index_seq2] = lcs_length_table[index_seq1 - 1][index_seq2]
                    direction_table[index_seq1][index_seq2] = 'U'
                else:
                    lcs_length_table[index_seq1][index_seq2] = lcs_length_table[index_seq1][index_seq2 - 1]
                    direction_table[index_seq1][index_seq2] = 'L'
    return lcs_length_table, direction_table


def print_lcs(direction_table, seq1, index_seq1, index_seq2):
    if index_seq1 == 0 or index_seq2 == 0:
        return
    if direction_table[index_seq1][index_seq2] == 'D':
        print_lcs(direction_table, seq1, index_seq1 - 1, index_seq2 - 1)
        print(seq1[index_seq1 - 1], end='')
    elif direction_table[index_seq1][index_seq2] == 'U':
        print_lcs(direction_table, seq1, index_seq1 - 1, index_seq2)
    else:
        print_lcs(direction_table, seq1, index_seq1, index_seq2 - 1)


# Example usage
seq1 = "abaaba"
seq2 = "babbab"
length_seq1 = len(seq1)
length_seq2 = len(seq2)
lcs_length_table, direction_table = compute_lcs_length_and_direction(seq1, seq2)
print("LCS Length Table:")
for row in lcs_length_table:
    print(row)
print("\nDirection Table:")
for row in direction_table:
    print(row)
print("\nLCS:")
print_lcs(direction_table, seq1, length_seq1, length_seq2)
print()
