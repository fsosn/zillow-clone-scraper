import pandas as pd
from constants import OUTPUT_DIRNAME, OUTPUT_FILENAME


def export_to_xlsx(df: pd.DataFrame):
    filepath = OUTPUT_DIRNAME + "/" + OUTPUT_FILENAME
    writer = pd.ExcelWriter(filepath, engine="xlsxwriter")
    df.rename(columns={"price": "price/month [$]"}, inplace=True)
    df.to_excel(writer, index=False, sheet_name="estate")
    worksheet = writer.sheets["estate"]
    for i, col in enumerate(df.columns):
        width = max(df[col].apply(lambda x: len(str(x))).max(), len(col))
        worksheet.set_column(i, i, width)
    writer.close()
