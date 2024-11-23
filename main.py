from fpdf import FPDF
import pandas as pd

# Initialize the PDF object
pdf = FPDF(orientation="P", unit="mm", format="A4")

# creating pandas data frames object
df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L")
    pdf.line(10, 21, 200, 21)

    for i in range(row["Pages"] -1):
        pdf.add_page()


pdf.output("output.pdf")

