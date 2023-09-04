# Exercise 8 - Merge the PDF | Python Tutorial - Day #76

#merging the pdf files 

from PyPDF2 import PdfFileMerger

import glob    #to print the file names

#printing the file names by using glob module

files=glob.glob('#100daysofcode/*.pdf')
print(files)

merger=PdfFileMerger

for file in files:
    merger.append(file)

merger.write('The_merged_file.pdf')
merger.close()

