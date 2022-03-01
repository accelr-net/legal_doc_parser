from lib.DocIterator import DocIterator
from lib.ParserBase import ParserBase
from lib.ParaParser import ParaParser
import re

pattern_level_1 = r'^\d+'r'\.'  # this is for 1. , 2. , 3.
pattern_3 = r'^.'r'\d+'r'.'  # this is for
pattern_level_2 = r'^\(\d+\)'  # this is for (1) , (2)
pattern_level_2_v2 = r'^\ 'r'\(\d+\)'  # this is for (1) , (2)
pattern_3_v2 = r'\d+'
pattern_level_3 = r'^\(([abcdefgh])\)' # (a)


def get_level_value(paragraph: str):
    print(paragraph)
    if re.findall(pattern_level_1, paragraph):
        return 1

    elif re.findall(pattern_level_2, paragraph):
        return 2

    elif re.findall(pattern_level_3, paragraph):
        return 3

    elif paragraph:
        return 4


class SectionParser:
    test_idx = 0
    test_data = [0, 1, 2, 2]

    def __init__(self, doc_iterator: DocIterator):
        self.child_list = []
        self.test_int = 0
        self.parse_doc(doc_iterator)

    def parse_doc(self, doc_iterator: DocIterator):
        while True:
            line = doc_iterator.peek_line()
            line_type = self.get_line_type(line)

            if line_type == 0:
                doc_iterator.get_char(3)
                p = SectionParser(doc_iterator)
                self.child_list.append(p)
            elif line_type == 1:
                p = SectionParser(doc_iterator)
                self.child_list.append(p)
            elif line_type == 2:
                break
            else:
                raise Exception("Unexpected para type in document")

    def get_line_type(self, line):
        SectionParser.test_idx += 1

        return SectionParser.test_data[SectionParser.test_idx]


    def get_dict(self):
        child_dict_list = []
        for child in self.child_list:
            child_dict_list.append(child.get_dict())

        dictionary = {
            "level": 1,
            "index": 0,
            "paragraphs": child_dict_list
        }
        return dictionary

    def print_list(self):
        print(self.child_list)
