from docx import Document


class HelperFile:

    def __init__(self, path_file, debug_mode_on):
        self.path_file = path_file
        self.debug_mode_on = debug_mode_on

    def get_text_from_file(self):
        doc_path = self.path_file

        doc = Document(doc_path)

        text_content = ""
        for paragraph in doc.paragraphs:
            text_content += paragraph.text + "\n"

        if self.debug_mode_on:
            print(text_content)

        return text_content
