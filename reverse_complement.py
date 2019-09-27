def reverse_complement(sequence):
    sequence=sequence.upper()
    sequence = reversed(sequence)
    new_seq=[]
    for char in sequence:
        if char == 'A':
            new_seq.append('T')
        elif char == 'T':
            new_seq.append('A')
        elif char == 'C':
            new_seq.append('G')
        elif char == 'G':
            new_seq.append('C')
        else:
            new_seq.append(char)
    return "".join(new_seq)