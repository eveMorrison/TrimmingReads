import re

trimming_info_File = open("reads_to_trim_dys.txt", "r")

for line in trimming_info_File:
   if re.search('^.+\d',line,0):
      values = line.split()
      id_dys = values[0]
      leng_dys = values[1]
      leng_split = values[5]
      #print(id_dys)
      #print(leng_dys)
      #print(leng_split)


linelist = trimming_info_File.readlines()
fileLeng = len(linelist)
 
trimming_info_File.close()