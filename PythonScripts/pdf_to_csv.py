import PyPDF2
import csv

csvFile = open('/Users/nrementeria/repos/_PERSONAL/MyToolbox/PythonScripts/data/Listado_Precios_Cuidados_2022.csv', 'w', encoding='UTF8')
#csvWrite = csv.writer(csvFile)

pdfFile = open('/Users/nrementeria/repos/_PERSONAL/MyToolbox/PythonScripts/data/Listado_Precios_Cuidados_2022.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

numberOfPages = pdfReader.numPages

currentPage = 1

while numberOfPages > currentPage:
  pageObj = pdfReader.getPage(currentPage-1)
  rawDataExtracted = pageObj.extractText()
  listDataExtracted = rawDataExtracted.split('\n')
  listDataExtracted = listDataExtracted[:-1]
  csvLine = ''
  i = 1
  for item in listDataExtracted:
    if i == 1 or i == 2 or i == 3:
      csvLine += item + ';'
      i = i + 1
    else:
      csvLine += item + "\n"
      csvFile.write(csvLine)
      i = 1
      csvLine = ''
  currentPage = currentPage + 1


csvFile.close()
pdfFile.close()