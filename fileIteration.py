from asyncore import read
from posixpath import split
import re
import math
from pprint import pprint
from Bio import SeqIO

fasta_file = "Dvir-dysgenic-all.fasta"
csv_file = "read.ids.dys_to_trim.final.txt"
#fasta_file = "Dys_reads_to_trim.fasta"
#csv_file = "reads_to_trim_dys.txt"

'''def find_fa_seq(fname, seq_ID, seq_len, seq_start, seq_end):
   with open(fname, "r") as fh:
      identifier = None
      sequence = []
      for line in fh:
         line = line.strip()  # Remove trailing newline characters.
         if line.startswith(">"):
            identifier = line.split()[0]
            #print(identifier)
            sequence = []
         else:
            if(identifier == seq_ID):
               sequence.append(line)
               sequence_str = "".join([str(item) for item in sequence])
               if(len(sequence_str) >= seq_len):
               	#print(len(sequence_str))
               	#print(sequence_str[seq_start:seq_end+1])
               	f.write(seq_ID + "\n" + sequence_str[seq_start:seq_end+1] + "\n")'''

def find_fa_seq_biopy(fname, seq_ID, seq_len, seq_start, seq_end):
   #with open("dys_reads_trimmed.fasta","a") as f:
        for seq_record in SeqIO.parse(fasta_file, "fasta"):
            if(str(">" + seq_record.id) == seq_ID):
                f.write(">" + str(seq_record.id) + "\n")
                #f.write(str(seq_record.seq) + "\n")
                f.write(str(seq_record.seq[seq_start:seq_end+1]) + "\n")

trimming_info_File = open(csv_file, "r")
f = open("dys_reads_trimmed.fasta", "a")

#find_fa_seq_biopy(csv_file, "echo")

for line in trimming_info_File:
   if re.search('^>',line,0):
      values = line.split()
      id_dys = values[0]
      leng_dys = int(values[1])
      leng_flank = float(values[5])
      sequence_start = math.ceil(leng_flank)
      sequence_end = leng_dys - math.floor(leng_flank)
      
      find_fa_seq_biopy(fasta_file,id_dys,leng_dys, sequence_start, sequence_end)
      #find_fa_seq(fasta_file,id_dys,leng_dys, sequence_start, sequence_end)
      #print(id_dys)
      #print(leng_dys)
      #print(leng_flank)
      #print(sequence_start)
      #print(sequence_end)

#get information on how long the file is
#linelist = trimming_info_File.readlines()
#fileLeng = len(linelist)
 
f.close() 
trimming_info_File.close()
