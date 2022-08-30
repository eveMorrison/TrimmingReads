import re

fasta_file = "Dys_reads_to_trim.fasta"
csv_file = "reads_to_trim_dys.txt"

def find_fa_seq(fname, seq_ID):
   with open(fname, "r") as fh:
      identifier = None
      sequence = []
      for line in fh:
         line = line.strip()  # Remove trailing newline characters.
         if line.startswith(">"):
            identifier = line
            print(identifier)
            sequence = []
         else:
            sequence.append(line)

trimming_info_File = open(csv_file, "r")

for line in trimming_info_File:
   if re.search('^>',line,0):
      values = line.split()
      id_dys = values[0]
      leng_dys = int(values[1])
      leng_flank = float(values[5])
      sequence_start = leng_flank
      sequence_end = leng_dys - leng_flank

      find_fa_seq(fasta_file,id_dys)
      #print(id_dys)
      #print(leng_dys)
      #print(leng_flank)
      #print(sequence_start)
      #print(sequence_end)

#get information on how long the file is
#linelist = trimming_info_File.readlines()
#fileLeng = len(linelist)
 
trimming_info_File.close()
