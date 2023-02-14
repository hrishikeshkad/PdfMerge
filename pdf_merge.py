import os
from PyPDF2 import PdfMerger, PdfReader

# Call the PdfMerger
mergedObject = PdfMerger()

path = "C:\\Users\\E0419226\\Documents\\Hrishikesh\\Personal\\DOP\\2023\\Feb\\12"
dir_list = os.listdir(path)

# Loop through all of them and append their pages
for file in dir_list:
    if ".pdf" in file:
        mergedObject.append(PdfReader(path + "\\"+ file, 'rb'))

# Write all the files into a file which is named as shown below
mergedObject.write(path + "\mergedfile.pdf")