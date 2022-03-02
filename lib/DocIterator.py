import re
from pyxpdf import Document


class DocIterator:
    pattern_space = r'^\ '
    counter = 0
    pdf_text_list = []
    current_point = 0

    def __init__(self) -> None:
        self.text_line = "hiii"
        self.counter_1 = 0
        self.final_line = ""

    def peek_word(self, section_status: int, para_type: str):
        print(para_type)
        if section_status == 1:
            DocIterator.current_point += 1
            self.final_line = DocIterator.pdf_text_list[DocIterator.current_point]
            print("section status 1")
        elif section_status == 2:
            self.final_line = DocIterator.pdf_text_list[DocIterator.current_point].split(para_type, 1)[1]
        else:
            self.final_line = DocIterator.pdf_text_list[DocIterator.current_point]

    @staticmethod
    def peek_word11():
        return DocIterator.pdf_text_list[DocIterator.current_point].strip()  # return removing spaces at front

    def get_word(self):
        print("in dociterator - " + self.final_line)
        if re.findall(DocIterator.pattern_space, self.final_line):
            self.final_line = self.final_line.split(" ", 1)[1]
        else:
            self.final_line = self.final_line
        return self.final_line.split()[0]

    def get_line(self):
        return self.final_line

    @staticmethod
    def split_to_paragraph(file_name: str):
        try:
            document = Document(file_name)
            full_text = document.text()
            DocIterator.pdf_text_list = full_text.split("\n")
            print(DocIterator.pdf_text_list)
        except TypeError:
            raise "error occure !"

    def couter_up(self):
        DocIterator.counter += 1
        print(DocIterator.counter)
