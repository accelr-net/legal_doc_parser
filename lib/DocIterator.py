import re
from builtins import Exception
from pyxpdf import Document


class DocIterator:
    pattern_space = r'^\ '

    def __init__(self, file_name : str) -> None:
        self.file_name = file_name
        self.pdf_text_list = []
        try:
            document = Document(file_name)
            full_text = document.text()
            self.pdf_text_list = full_text.split("\n")
            print(self.pdf_text_list)
        except TypeError:
            raise Exception("Unable to process document {}!".format(file_name))

    def peek_word(self):
        if len(self.pdf_text_list) == 0:
            return ""
        return self.pdf_text_list[0].split()[0]

    def get_word(self):
        if len(self.pdf_text_list) == 0:
            return ""
        result = self.pdf_text_list[0].split()[0]
        self.pdf_text_list[0] = self.pdf_text_list[0][len(result)+1:]
        return result

    def get_line(self):
        if len(self.pdf_text_list) == 0:
            return ""
        result = self.pdf_text_list[0]
        self.pdf_text_list.pop(0)
        return result
