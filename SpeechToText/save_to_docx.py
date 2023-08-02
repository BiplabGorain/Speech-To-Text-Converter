from docx import Document


def write_docx(notes):
    document = Document()
    document.add_paragraph(notes)
    document.save("./Notes.docx")
