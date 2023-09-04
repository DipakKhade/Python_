# Exercise 8 - Merge the Pdf Solution in Python | Python Tutorial - Day #82

# day 76


from pypdf import PdfWriter
import os

merger = PdfWriter()
files=[file for file in os.listdir() if file.endswith('.pdf') ]


for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf Distributions.pdf")
merger.close()
