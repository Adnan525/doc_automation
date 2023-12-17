from docx import Document
from datetime import datetime
from data_collection_util import collect_data_master, collect_data

 # dd-mm-yyyy format
current_date = datetime.now().strftime("%d-%m-%Y")
# day
current_day = datetime.now().strftime("%A")

def _print_table_contents(table):
    for row_idx, row in enumerate(table.rows):
        for col_idx, cell in enumerate(row.cells):
            print(f"Row {row_idx}, Column {col_idx}: {cell.text}")

def _update_table_cell(table, row_index, col_index, new_value):
    """
        Row 1, Column 0: DATE
        Row 1, Column 3: DAY
        Row 2, Column 0: SECURITY OFFICER
        Row 2, Column 2: LICENSE NO.
        Row 3, Column 0: START TIME
        Row 3, Column 2: FINISH TIME

    """
    table.cell(row_index, col_index).text = new_value

def update_template(template_path, output_path):

    # template
    template_doc = Document(template_path)

    # Update date and day in the first table
    first_table = template_doc.tables[0]
    # _print_table_contents(first_table)
    _update_table_cell(first_table, 1, 1, current_date)
    _update_table_cell(first_table, 1, 3, current_day)

    # second table 
    second_table = template_doc.tables[1]
    # _print_table_contents(second_table)

    # delete the rows except the first one
    for row in second_table.rows[1:]:
        second_table._element.remove(row._element)

    # Save the modified document
    template_doc.save(output_path)

if __name__ == "__main__":
    data = collect_data_master()

    # template document
    template_path = "template.docx"

    # output file
    output_summary = "output_document.docx"
    # date file
    output_shift = f"{current_date}.docx"

    # Update the template and save the modified document
    update_template(template_path, output_summary)
    update_template(template_path, output_shift)

    print(f"Modified document saved as: {output_summary} and {output_shift}")
