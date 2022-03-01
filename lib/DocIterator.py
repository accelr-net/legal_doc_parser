import re


class DocIterator:
    pattern_space = r'^\ '

    def __init__(self, file_name: str) -> None:
        self.text_line = file_name

    def peek_line(self):
        return self.text_line.split(" ", 1)[1]  # return removing spaces at front

    def get_char(self, num_car: int):

        if re.findall(DocIterator.pattern_space, self.text_line):
            final_line = self.text_line.split(" ", 1)[1]
        else:
            final_line = self.text_line
        return final_line.split()[0]

    def get_line(self):
        return "here is the text"
