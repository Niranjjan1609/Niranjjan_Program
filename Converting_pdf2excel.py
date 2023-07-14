import PyPDF2 # pip install PyPDF2 # 22
# import tabula # pip install tabula-py


import os

def split_pdf(input_path, output_path):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)

        # Create the output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        for page_number in range(total_pages):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_number])

            output_file_path = os.path.join(output_path, f"Page_{page_number + 1}.pdf")
            with open(output_file_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            print(f"Page {page_number + 1} saved as {output_file_path}")


def split_pdf_duplicate(input_path, output_path):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)
		pages = [185,197,202,219,238,243,249,255,256,265]

        # Create the output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        for page_number in pages:
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_number])

            output_file_path = os.path.join(output_path, f"Page_{page_number + 1}.pdf")
            with open(output_file_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            print(f"Page {page_number + 1} saved as {output_file_path}")



def convert_pdf_to_excel(input_path, output_path):
    # Read PDF and extract tables
    tables = tabula.read_pdf(input_path, pages='all')

    # Export each table to separate Excel file
    for i, table in enumerate(tables):
        table.to_excel(f"{output_path}_{i + 1}.xlsx", index=False)
        print(f"Table {i + 1} saved as {output_path}_{i + 1}.xlsx")


# Usage example
input_path = 'C:\\Users\\Niruj\\Downloads\\New folder\\Telephone Book 6-2-19.pdf'
output_path = 'C:\\Users\\Niruj\\Downloads\\output-123\\Test'

split_pdf(input_path, output_path)
split_pdf_duplicate(input_path, output_path)

# convert_pdf_to_excel(input_path, output_path)
