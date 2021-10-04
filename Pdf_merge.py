from os import listdir, mkdir, startfile
from os.path import isfile, join, exists
from PyPDF2 import PdfFileMerger

# Input file path and print the pdf files in that path
path = input("Enter the Folder location: ")
pdfFiles = [f for f in listdir(path) if isfile(join(path, f)) and '.pdf' in f]
print('\nPDF Files:\n')
for file in pdfFiles:
    print(file)

# Input the name of the output file
resultFile = input("\nEnter the name of the output file : ")
if '.pdf' not in resultFile:
    resultFile += '.pdf'

# Append the pdf files
merger = PdfFileMerger()
for pdf in pdfFiles:
    merger.append(path + '\\' + pdf)

# If the Output directory does not exist then create one
if not exists(path + '\\Output'):
    mkdir(path + '\\Output')

# Write the merged result file to the Output directory
merger.write(path + '\\Output\\' + resultFile)
merger.close()

# Launch the result file
print('\n Wow!! Your file ' + resultFile, 'Successfully created!! at this location: ', path + '\\Output\\')
startfile(path + '\\Output\\' + resultFile)
