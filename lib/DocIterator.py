from builtins import Exception
from pyxpdf import Document


class DocIterator:
    pattern_space = r'^\ '

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.pdf_text_list = []
        try:
            document = Document(file_name)
            full_text = document.text()
            list_doc = full_text.split("\n")
            for element in list_doc:
                if element.strip():
                    self.pdf_text_list.append(element)
            print(self.pdf_text_list)
        except TypeError:
            raise Exception("Unable to process document {}!".format(file_name))

    def peek_word(self):
        if self.pdf_text_list:
            if len(self.pdf_text_list[0]) == 0:
                return ""
            else:
                return self.pdf_text_list[0].split()[0]
        else:
            return "final@doc@harshana"

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
