from Helpers import HelperFile as Hf

if __name__ == "__main__":
    file_folder = "C:\\Projetos\\Python\\EmailSending\\BaseContract\\Contract.docx"
    helper_file_class = Hf.HelperFile(file_folder, True)
    helper_file_class.get_text_from_file()
