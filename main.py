from Bio import Entrez, SeqIO

# NCBI 데이터베이스에 접속하기 위한 이메일 주소를 입력해주세요.
Entrez.email = "lunarari0301@gmail.com"

# SARS-CoV-2의 염기 서열을 다운로드합니다.
handle = Entrez.efetch(db="nucleotide", id="NC_045512", rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
sars_cov2_seq = str(record.seq)

# 대조할 염기 서열을 gene.txt로부터 가져옵니다.
f = open("gene.txt", 'r')
user_seq = f.readline()
f.close()

# 두 염기 서열을 비교합니다.
if sars_cov2_seq == user_seq:
    print("입력한 염기 서열과 SARS-CoV-2의 염기 서열이 일치합니다.")
else:
    print("입력한 염기 서열과 SARS-CoV-2의 염기 서열이 일치하지 않습니다.")