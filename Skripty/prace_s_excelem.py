# pip install openpyxl
# watch out for system path
# command pallete -> select interpreter python
import openpyxl
wb_obj = openpyxl.Workbook()

# Read the active sheet:
sheet = wb_obj.active

cislo = 1
for radek in range(1,10):
    for sloupec in range(1,10):
        sheet.cell(row=radek, column=sloupec).value = cislo
        cislo += 1

cesta = "C:\\Users\\StudentEN\\Desktop\\Skripty\\test.xlsx"
wb_obj.save(filename = cesta)