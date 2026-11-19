import pandas as pd
from openpyxl import load_workbook

def export_to_template(df, template_path, output_path):
    writer = pd.ExcelWriter(output_path, engine="openpyxl")
    book = load_workbook(template_path)
    writer.book = book
    writer.sheets = {ws.title: ws for ws in book.worksheets}
    df.to_excel(writer, sheet_name="汇总", index=False)
    writer.close()
