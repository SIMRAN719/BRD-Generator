from fpdf import FPDF

def create_pdf(text, output_file='output.pdf'):
    output_file = "Output/"+output_file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True, align='L')
    pdf.output(output_file)

def text_to_file(text, output_file='output.txt'):
    output_file = "Output/"+output_file
    with open(output_file, 'w') as f:
        f.write(text)