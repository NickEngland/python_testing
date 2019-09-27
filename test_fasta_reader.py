import fasta_reader


def test_fasta_reader_strips_newlines():
    header, seq = next(fasta_reader.read_fasta_generator("test.fasta"))
    print(header[-1])
    assert "\n" != header[-1]


def test_fasta_reader():
    results = []
    for entries in fasta_reader.read_fasta_generator("test.fasta"):
        results.append(entries)
    print(results)
    assert 3 == len(results)


def test_headers():
    expected_headers = ["seq1", "seq2", "seq3"]
    found_headers = []
    for header, seq in fasta_reader.read_fasta_generator("test.fasta"):
        found_headers.append(header)
    assert expected_headers == found_headers
