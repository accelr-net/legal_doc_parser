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

    def __init__(self, doc_iterator: DocIterator, level=0):
        self.type_name = None
        self.level = level
        self.child_list = []
        self.test_int = 0
        self.name = ""
        self.parse_doc(doc_iterator)

    def parse_doc(self, doc_iterator: DocIterator):
        while True:
            # paragraph_text = doc_iterator.peek_word()
            print("while loop")
            paragraph_type = self.get_para_type(doc_iterator.peek_word())

            if paragraph_type == ParaType.PARA_TYPE_SECTION:
                self.name = doc_iterator.get_word()
                print("Again a section ")
                p = SectionParser(doc_iterator, self.level + 1)
                self.child_list.append(p)
            elif paragraph_type == ParaType.PARA_TYPE_PARA:
                print("in the paragraph")
                p = ParaParser(doc_iterator)
                self.child_list.append(p)
            elif paragraph_type == ParaType.PARA_TYPE_END_SECTION:
                break
            else:
                raise Exception("Unexpected para type in document")

    def get_para_type(self, paragraph):
        print(paragraph + " getting -para-type")
        if self.level == SectionParser.LEVEL_0:
            print("Came to LEVEL_0")
            if re.findall(SectionParser.PATTERN_LEVEL_1, paragraph):
                print("Came to LEVEL_0 patter 1. , 2.")
                return ParaType.PARA_TYPE_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_2, paragraph) or re.findall(SectionParser.PATTERN_LEVEL_3, paragraph):
                print("came level 1")
                return ParaType.PARA_TYPE_ERROR
            elif paragraph:
                return ParaType.PARA_TYPE_PARA
            else:
                return ParaType.PARA_TYPE_ERROR
        elif self.level == SectionParser.LEVEL_1:
            print("Came to LEVEL_1")
            if re.findall(SectionParser.PATTERN_LEVEL_1, paragraph):
                return ParaType.PARA_TYPE_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_2, paragraph):
                print("Came to LEVEL_1 pattern (1) , (2)")
                return ParaType.PARA_TYPE_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_3, paragraph):
                return ParaType.PARA_TYPE_ERROR
            elif paragraph:
                print("Came to LEVEL_1 paragraph")
                return ParaType.PARA_TYPE_PARA
            else:
                return ParaType.PARA_TYPE_ERROR
        elif self.level == SectionParser.LEVEL_2:
            print("Came to LEVEL_2")
            if re.findall(SectionParser.PATTERN_LEVEL_1, paragraph):
                return ParaType.PARA_TYPE_SECTION
            elif re.findall(SectionParser.PATTERN_LEVEL_2, paragraph):
                return ParaType.PARA_TYPE_ERROR
            elif re.findall(SectionParser.PATTERN_LEVEL_3, paragraph):
                return ParaType.PARA_TYPE_ERROR
            elif paragraph:
                print("Came to LEVEL_2 pattern paragraph")
                return ParaType.PARA_TYPE_PARA
            else:
                return ParaType.PARA_TYPE_ERROR
        else:
            return ParaType.PARA_TYPE_ERROR

    def get_dict(self):
        child_dict_list = []
        for child in self.child_list:
            child_dict_list.append(child.get_dict())

        dictionary = {
            "level": self.level,
            "section_name" : self.name,
            "name": self.type_name,
            "paragraphs": child_dict_list
        }
        return dictionary

    def print_list(self):
        print(self.child_list)
