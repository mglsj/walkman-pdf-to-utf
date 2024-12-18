from docx import Document

from walkmanchanakya_2_utf import convertToUni

HINDI_FALLBACK_FONT = "Arial"


# Process Word Document
def process_word_file(input_file_path, output_file_path):
    # Load the Word file
    doc = Document(input_file_path)

    # Iterate through paragraphs and runs
    for para in doc.paragraphs:
        for run in para.runs:
            if (
                run.font.name == HINDI_FALLBACK_FONT
            ):  # Check if font is Arial (Hindi text)
                run.text = convertToUni(run.text, 1)  # Convert to Unicode
            # elif run.font.name == "Times New Roman":  # English text, keep as is
            # pass  # No changes required

    # Save the processed file
    doc.save(output_file_path)
