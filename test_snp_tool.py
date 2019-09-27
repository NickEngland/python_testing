import snp_tool

def test_get_reading_frame():
    assert 1 == snp_tool.get_reading_frame(1)
    assert 2 == snp_tool.get_reading_frame(2)
    assert 3 == snp_tool.get_reading_frame(3)
    assert 1 == snp_tool.get_reading_frame(55)

def test_are_snps_in_exon():
    list = [1, 2, 3 ,55, 56]
    results = snp_tool.are_snps_in_exon(list)
    assert [1, 2 ,3,55 ] == results
    list = [1]
    results = snp_tool.are_snps_in_exon(list)
    assert [1] == results

def test_range_not_working():
    assert [1] == snp_tool.are_snps_in_exon([1])
    assert [1] == snp_tool.are_snps_in_exon(range(2))