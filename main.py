#! C:\Users\Mario\Desktop\python\pdf-template\venv\Scripts\python.exe
from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("./topics.csv")
pdf_page = 0
for index, row in df.iterrows():    
    for i in range(row["Pages"]):
        pdf_page += 1
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 22, 200, 22)
        
        # Setting the footer
        pdf.ln(255)
        pdf.set_text_color(180,180,180)
        pdf.set_font(family="Times", style="B", size=12)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="L")
        pdf.cell(w=0, h=10, txt=f"Page {str(pdf_page)}", align="R")

pdf.output("output.pdf")
