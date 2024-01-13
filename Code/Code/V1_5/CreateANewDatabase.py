from openpyxl import Workbook

name = str(input("What is the name of the file:"))

def create_workbook(path):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Box Id"

    sheet["B1"] = "Building"

    sheet["C1"] = "Row"

    sheet["D1"] = "level"

    sheet["E1"] = "Size"

    sheet["F1"] = "Owner"

    sheet["G1"] = "Description"

    workbook.save(path)

create_workbook(f"{name}.xlsx")

