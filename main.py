import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def split_pdf(pdf_path, output_folder):
    if not os.path.exists(pdf_path):
        messagebox.showerror("Error", "El archivo PDF no existe.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)
        
        for i in range(num_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])
            
            output_filename = os.path.join(output_folder, f"pagina_{i+1}.pdf")
            with open(output_filename, "wb") as output_file:
                writer.write(output_file)
            
    messagebox.showinfo("Completado", f"PDF separado en {num_pages} páginas")

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        output_folder = os.path.join(os.path.dirname(file_path), "paginas_separadas")
        split_pdf(file_path, output_folder)

def main():
    root = tk.Tk()
    root.withdraw()
    select_pdf()

if __name__ == "__main__":
    main()
