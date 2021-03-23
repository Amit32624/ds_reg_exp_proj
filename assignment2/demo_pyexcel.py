
# For documentation see http://docs.pyexcel.org/en/latest/
# Warning: documentation not especially beginner friendly.
# Code below is deliberately overcommented for reference.

import pyexcel as pe

# Code can cope with either .xlsx or .ods spreadsheets. Other
# formats may require extra plugins to be installed.
#FILE_NAME = "exam_list_ods_format.ods"
FILE_NAME = "exam_list_xlsx_format.xlsx"

# Extract Book object from file.
book = pe.get_book(file_name = FILE_NAME)

# Extract Sheets from book as dictionary with sheet names as
# keys and sheet contends as list of lists.
all_sheets = book.to_dict()
print("Sheets: ", list(all_sheets.keys()))


#main_sheet = all_sheets["Sheet1"]
#print("Sheet as list of lists:")
#print(main_sheet)
#print("Top left cell: ", main_sheet[0][0])
#main_sheet[0][0] = "mOdUlE cOdE"
#print("Top left cell: ", main_sheet[0][0])

# Extract the first sheet within workbook by name.
sname = list(book.to_dict())[0]
sheet = book[sname]
print("Sheet '%s' of type %s:" % (sname, type(sheet)))
print(sheet.content)
print("Num rows: ", sheet.number_of_rows())
print("Num columns: ", sheet.number_of_columns())

# Access a random cell by coords (top eft is (0, 0)).
print(sheet[2, 1])
sheet[2, 1] = "Intermediate Nohtyp"

# Access a random cell by Excel coords (top left is A1).
print(sheet["B3"])

# Access a complete row or a column.
print("Row 2: ", sheet.row[2])
print("Column 1: ", sheet.column[1])

# Use Row 0 as column headings; refer to columns by name
sheet.name_columns_by_row(0)
codes = sheet.column["Module Code"]
print("Modules are: ", codes)
print(sheet.column["Module Code"][1])

# Iterate through rows one ny one.
records = sheet.to_records()
for r in records:
    print("Module %s is taught by %s." % (r["Module Code"], r["Lecturer"]))

# Change the sheet's name.
sheet.name = "Tuesday"

# Add a fresh row.
sheet.row += ["CS4567", "Small Data", "Prof. Greene"]
print(sheet)

# Add a fresh column
sheet.column += [None, [5, 5, 5, 5]]
print(sheet)


# Save the sheet.
book.save_as("new_"+FILE_NAME)
