import time
from pprint import pprint
from Bio import SeqIO

startTime = time.time()

fasta_file = "Dys_reads_to_trim.fasta"
f = open("dys_reads_trimmed.fasta", "a")

#####your python script#####
for seq_record in SeqIO.parse(fasta_file, "fasta"):
    '''if(str(">" + seq_record.id) == seq_ID):
        f.write(">" + str(seq_record.id) + "\n")
        #f.write(str(seq_record.seq) + "\n")
        f.write(str(seq_record.seq[seq_start:seq_end+1]) + "\n")'''

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))