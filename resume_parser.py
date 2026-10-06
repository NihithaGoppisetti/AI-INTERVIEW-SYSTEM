from pypdf import PdfReader


class ResumeParser:

    def __init__(self):
        pass

    def extract_text(self, uploaded_file):

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text