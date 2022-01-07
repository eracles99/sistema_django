import openpyxl
book=openpyxl.load_workbook('reporte carga academica.xlsx',data_only=True)

hoja=book.active

datos=hoja['C3':'O9']


for fila in datos:
    print([datos.value for datos in fila])