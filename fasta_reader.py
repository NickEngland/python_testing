"""
Function to read a fasta file and give a generator for header, seq tuple.
"""


def read_fasta_generator(file):
    with open(file) as file_handler:
        sequence = []
        header = None
        for line in file_handler:
            if line.startswith(">"):
                if header is None:
                    header = line[1:].strip()
                else:
                    yield (header, "".join(sequence))
                    header = line[1:].strip()
                    sequence = []
            else:
                sequence.append(line.strip())
        yield (header, "".join(sequence))
