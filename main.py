from Bio import Entrez, SeqIO

def get_sars_cov_2_sequence():
    Entrez.email = "lunarari0301@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id="NC_045512.2", rettype="fasta")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return str(record.seq)

def calculate_similarity(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("The lengths of two sequences are not equal.")
    count = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            count += 1
    similarity = count / len(seq1)
    return similarity

#user_sequence = input("Enter the DNA sequence: ")
sars_cov_2_sequence = get_sars_cov_2_sequence()
'''
f = open('gene2.txt', 'w')
f.write(sars_cov_2_sequence)
f.close()
'''
f = open('gene2.txt', 'r')
user_sequence = f.read()
f.close()

similarity = calculate_similarity(user_sequence, sars_cov_2_sequence)

print(f"The similarity between the user sequence and SARS-CoV-2 sequence is:{similarity*100 :.2f}%", )