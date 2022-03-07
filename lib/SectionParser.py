from enum import Enum
import re
from lib.DocIterator import DocIterator
from lib.ParserBase import ParserBase
from lib.ParaParser import ParaParser


class ParaType(Enum):
    PARA_TYPE_SECTION = 0
    PARA_TYPE_PARA = 1
    PARA_TYPE_END_SECTION = 2
    PARA_TYPE_ERROR = 3


class SectionParser:
    PATTERN_LEVEL_1 = r'^\d+'r'\.'  # this is for 1. , 2. , 3.
    PATTERN_3 = r'^.'r'\d+'r'.'  # this is for
    PATTERN_LEVEL_2 = r'^\(\d+\)'  # this is for (1) , (2)
    PATTERN_LEVEL_2_V2 = r'^\ 'r'\(\d+\)'  # this is for (1) , (2)
    PATTERN_3_V2 = r'\d+'
    PATTERN_LEVEL_3 = r'^\(([abcdefgh])\)'  # (a)

    LEVEL_0 = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3

    def __init__(self, doc_iterator: DocIterator, para_pattern: str, level=0):
        self.type_name = None
        self.level = level
        self.child_list = []
        self.test_int = 0
        self.name = "hii"
        self.paragraph_text = para_pattern
        self.parse_doc(doc_iterator)

    def parse_doc(self, doc_iterator: DocIterator):
        while True:
            self.name = doc_iterator.peek_word()
            paragraph_type = self.get_para_type(doc_iterator.peek_word())
            if paragraph_type == ParaType.PARA_TYPE_SECTION:
                self.name = doc_iterator.get_word()
                p = SectionParser(doc_iterator, self.name, self.level + 1)
                self.child_list.append(p)
            elif paragraph_type == ParaType.PARA_TYPE_PARA:
                p = ParaParser(doc_iterator)
                self.child_list.append(p)
            elif paragraph_type == ParaType.PARA_TYPE_END_SECTION:
                break
            else:
                break
                raise Exception("Unexpected para type in document")

    def get_para_type(self, paragraph):
        if self.level == SectionParser.LEVEL_0:
            print("Came to LEVEL_0- " + self.name)
            if re.findall(SectionParser.PATTERN_LEVEL_1, paragraph):
                print("Text contains pattern 1. , 2.")
                return ParaType.PARA_TYPE_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_2, paragraph) or re.findall(SectionParser.PATTERN_LEVEL_3, paragraph):
                print("Text contains pattern (1) or (a) ..")
                return ParaType.PARA_TYPE_ERROR
            elif paragraph == "final@doc@harshana":
                return ParaType.PARA_TYPE_END_SECTION
            elif paragraph:
                print("Text contains pattern para")
                return ParaType.PARA_TYPE_PARA
            else:
                return ParaType.PARA_TYPE_ERROR
        elif self.level == SectionParser.LEVEL_1:
            print("Came to LEVEL_1- " + self.name)
            if re.findall(SectionParser.PATTERN_LEVEL_1, paragraph):
                print("Text contains pattern 1. , 2.")
                return ParaType.PARA_TYPE_END_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_2, paragraph):
                print("Text contains pattern (1)")
                return ParaType.PARA_TYPE_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_3, paragraph):
                return ParaType.PARA_TYPE_ERROR
            elif paragraph == "final@doc@harshana":
                return ParaType.PARA_TYPE_END_SECTION
            elif paragraph:
                print("Came to LEVEL_1 paragraph")
                return ParaType.PARA_TYPE_PARA
            else:
                print("Came to LEVEL_1 null")
                return ParaType.PARA_TYPE_END_SECTION
        elif self.level == SectionParser.LEVEL_2:
            print("Came to LEVEL_2- " + self.name)
            if re.findall(SectionParser.PATTERN_LEVEL_1, paragraph):
                print("Text contains pattern 1. , 2.")
                return ParaType.PARA_TYPE_END_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_2, paragraph):
                return ParaType.PARA_TYPE_END_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_3, paragraph):
                return ParaType.PARA_TYPE_SECTION
            elif paragraph == "final@doc@harshana":
                return ParaType.PARA_TYPE_END_SECTION
            elif paragraph:
                print("pattern paragraph")
                return ParaType.PARA_TYPE_PARA
            else:
                return ParaType.PARA_TYPE_END_SECTION
        elif self.level == SectionParser.LEVEL_3:
            print("Came to LEVEL_3- " + self.name)
            if re.findall(SectionParser.PATTERN_LEVEL_1, paragraph):
                print("Text contains pattern 1. , 2.")
                return ParaType.PARA_TYPE_END_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_2, paragraph):
                return ParaType.PARA_TYPE_END_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_3, paragraph):
                return ParaType.PARA_TYPE_END_SECTION
            elif paragraph:
                print("Came to LEVEL_3 pattern paragraph")
                return ParaType.PARA_TYPE_PARA
            else:
                return ParaType.PARA_TYPE_ERROR
        else:
            return ParaType.PARA_TYPE_ERROR

    def get_dict(self):
        child_dict_list = []
        for child in self.child_list:
            print(child)
            child_dict_list.append(child.get_dict())

        dictionary = {
            "level": self.level,
            "section_name": self.paragraph_text,
            "name": self.type_name,
            "list": child_dict_list
        }
        return dictionary

    def print_list(self):
        print(self.paragraph_text)



