from pypdf import PdfWriter
import io

def merge_pdfs(input_pdf_paths, output_pdf_path):
    """
    Merges a list of PDF files into a single output PDF.

    :param input_pdf_paths: A list of paths (strings) to the PDF files to be merged, 
                            in the order they should appear.
    :param output_pdf_path: The path where the combined PDF file will be saved.
    """
    # Create a PdfWriter object
    merger = PdfWriter()

    print("Starting PDF merge process...")
    
    # Loop through the list of input PDF file paths
    for path in input_pdf_paths:
        try:
            print(f"Adding pages from: {path}")
            # Append the entire PDF (all pages) to the merger object
            merger.append(path)
        except FileNotFoundError:
            print(f"Error: The file '{path}' was not found. Skipping.")
        except Exception as e:
            print(f"An error occurred while processing '{path}': {e}")
            
    # Write the merged PDF content to the output file
    try:
        with open(output_pdf_path, "wb") as output_file:
            merger.write(output_file)
        print(f"\n✅ Success: All PDFs merged and saved as: {output_pdf_path}")
        
    except Exception as e:
        print(f"\n❌ Error writing the output file: {e}")
        
    finally:
        # Close the merger object and any file handles it opened
        merger.close()

# --- Example Usage ---

# 1. Define the input files (in the desired order)
pdf_files = [
   
   "E:\\document E\\college\\notse\\sem 4\\MC\\MC.pdf",
   "E:\\document E\\college\\notse\\sem 4\\mc23.pdf"
]


# 2. Define the output file name
final_document = "E:\\document E\\college\\notse\\sem 4\\MC\\MC.pdf"

# --- Setup for testing (You must create these dummy files for the code to run) ---
# import fpdf
# # Create dummy PDF files for the example
# for i, filename in enumerate(pdf_files):
#     pdf = fpdf.FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt=f"This is page 1 of {filename}", ln=True, align="C")
#     pdf.add_page()
#     pdf.cell(200, 10, txt=f"This is page 2 of {filename}", ln=True, align="C")
#     pdf.output(filename)
#     print(f"Created dummy file: {filename}")
# # --- End of Setup ---

# 3. Run the merge function
merge_pdfs(pdf_files, final_document)