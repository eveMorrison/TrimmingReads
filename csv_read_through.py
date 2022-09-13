import time
import re
import math

startTime = time.time()

csv_file = "read.ids.dys_to_trim.final.txt"
trimming_info_File = open(csv_file, "r")

for line in trimming_info_File:
   if re.search('^>',line,0):
      values = line.split()
      id_dys = values[0]
      leng_dys = int(values[1])
      leng_flank = float(values[5])
      sequence_start = math.ceil(leng_flank)
      sequence_end = leng_dys - math.floor(leng_flank)
      
      #find_fa_seq(fasta_file,id_dys,leng_dys, sequence_start, sequence_end)
      #print(id_dys)
      #print(leng_dys)
      #print(leng_flank)
      #print(sequence_start)
      #print(sequence_end)

#get information on how long the file is
#linelist = trimming_info_File.readlines()
#fileLeng = len(linelist)

trimming_info_File.close()

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))