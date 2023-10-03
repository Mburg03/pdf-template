#! C:\Users\Mario\Desktop\python\pdf-template\venv\Scripts\python.exe
from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("./topics.csv")
pdf_page = 0

for index, row in df.iterrows():    
    for i in range(row["Pages"]):
        line_height = 22        
        pdf_page += 1
        
        # Creating pages
        pdf.add_page()
        pdf.set_draw_color(0,0,0)
        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 22, 200, 22)
        
        # Creating writelines
        for i in range(25):
            line_height += 10
            pdf.set_draw_color(180,180,180)
            pdf.line(15, line_height, 195, line_height)

        # Setting the footer of the pdf file
        pdf.ln(260)
        pdf.set_text_color(180,180,180)
        pdf.set_font(family="Times", style="B", size=12)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="L")
        pdf.cell(w=0, h=10, txt=f"Page {str(pdf_page)}", align="R")

pdf.output("notebook.pdf")