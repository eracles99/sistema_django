import openpyxl

book=openpyxl.load_workbook('reporte carga academica.xlsx',data_only=True)

hoja=book.active

celdas=hoja['C3':'O9']

for fila in celdas:
    print(len(fila))
