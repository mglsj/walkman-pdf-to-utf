import os
from google_cloud_convert import convert_pdf_to_google_doc
from font_convert import process_word_file


# Comment this loop if you want to skip pdf conversion
for file in os.listdir("input"):
    if file.endswith(".pdf"):
        print("\nConverting", file, "to .docx")
        convert_pdf_to_google_doc(
            "input/" + file, "raw/" + file.removesuffix(".pdf") + ".docx"
        )

for file in os.listdir("raw"):
    if file.endswith(".docx"):
        print("\nProcessing file: " + file)
        process_word_file("raw/" + file, "output/" + file)
        print(f"File processed: {file}")
