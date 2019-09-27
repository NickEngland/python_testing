
def snp_finder(reference, sequence):
    snps = []
    for i,char in enumerate(reference):
        ref_char = char
        seq_char = sequence[i]
        if(ref_char != seq_char):
            snps.append(i+1)
    return snps


def are_snps_in_exon(snps):
    snps_in_exon =[]
    for snp in snps:
        if snp <= 55 and snp >= 1:
            snps_in_exon.append(snp)
        elif snp>=70 and snp <= 140:
            snps_in_exon.append(snp)
    return snps_in_exon

"""
Gets the reading frame for position (starting from 1)
"""
def get_reading_frame(pos):
    positions_in_exons = are_snps_in_exon(range(pos+1))
    mod =(len(positions_in_exons)-1) % 3
    #mod=(pos-1) % 3
    return mod+1

if __name__ == '__main__':
    snps=snp_finder("TTGGTGATGAAATCCCACAGGAAATCCTGGAAGAGCGCGTGCGCGCGGCGTTTGCCTTCCCGGCTCCGGTCGCCAATGTTGAAAGCGATGTCGGTTGTCTGGAATTGTTCCACGGGCCAACGCTGGCATTTAAAGATTTC"
                   ,"TTGGTGATGAAATCCCTCAGGAAATCCTGGAAGAGGGCGTGCGCGCGGCGTTTGCCATCCCGGCTGCGGTCGCCAATTTTGAAAGCGATGTCCGTTGTCTGGAATTGTTGCACGGGCCAACGCTGGCAATTAAAGATTTC")
    print(snps)
    exon=are_snps_in_exon(snps)
    print(exon)
    for exon_snp in exon:
        print("Frame: ",get_reading_frame(exon_snp)," pos ",exon_snp)