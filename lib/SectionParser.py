from lib.DocIterator import DocIterator
from lib.ParserBase import ParserBase
from lib.ParaParser import ParaParser
import re

pattern_level_1 = r'^\d+'r'\.'  # this is for 1. , 2. , 3.
pattern_3 = r'^.'r'\d+'r'.'  # this is for
pattern_level_2 = r'^\(\d+\)'  # this is for (1) , (2)
pattern_level_2_v2 = r'^\ 'r'\(\d+\)'  # this is for (1) , (2)
pattern_3_v2 = r'\d+'
pattern_level_3 = r'^\(([abcdefgh])\)'  # (a)


# def get_level_value(paragraph: str):
#     print(paragraph)
#     if re.findall(pattern_level_1, paragraph):
#         return 1
#
#     elif re.findall(pattern_level_2, paragraph):
#         return 2
#
#     elif re.findall(pattern_level_3, paragraph):
#         return 3
#
#     elif paragraph:
#         return 4


class SectionParser:
    # TODO : move to enum class
    PARA_TYPE_SECTION = 0
    PARA_TYPE_PARA = 1
    PARA_TYPE_END_SECTION = 2
    PARA_TYPE_ERROR = 3

    LEVEL_0 = 0
    LEVEL_1 = 1
    LEVEL_2 = 2

    def __init__(self, doc_iterator: DocIterator, level=0):
        self.type_name = None
        self.level = level
        self.child_list = []
        self.test_int = 0
        self.parse_doc(doc_iterator)

    def parse_doc(self, doc_iterator: DocIterator):
        while True:
            # paragraph_text = doc_iterator.peek_word()
            print("while loop")
            paragraph_type = self.get_para_type(doc_iterator.get_word())

            if paragraph_type == SectionParser.PARA_TYPE_SECTION:
                print("Again a section ")
                print(doc_iterator.get_word())
                doc_iterator.peek_word(2, doc_iterator.get_word())
                p = SectionParser(doc_iterator, self.level + 1)
                self.child_list.append(p)

            elif paragraph_type == SectionParser.PARA_TYPE_PARA:
                print("in the paragraph")
                #print(doc_iterator.get_word())
                #doc_iterator.peek_word(2, " ")
                #p1 = ParaParser(doc_iterator)
                #self.child_list.append(p1)
                print("final here")
                break

            elif paragraph_type == SectionParser.PARA_TYPE_END_SECTION:
                break
            else:
                raise Exception("Unexpected para type in document")

    def get_para_type(self, paragraph):
        print(paragraph + " getting -para-type")
        if self.level == SectionParser.LEVEL_0:
            print("Came to LEVEL_0")
            if re.findall(pattern_level_1, paragraph):
                print("Came to LEVEL_0 patter 1. , 2.")
                return SectionParser.PARA_TYPE_SECTION
            elif re.findall(pattern_level_2, paragraph) or re.findall(pattern_level_3, paragraph):
                print("came level 1")
                return SectionParser.PARA_TYPE_ERROR
            elif paragraph:
                return SectionParser.PARA_TYPE_PARA
            else:
                return SectionParser.PARA_TYPE_ERROR
        elif self.level == SectionParser.LEVEL_1:
            print("Came to LEVEL_1")
            if re.findall(pattern_level_1, paragraph):
                return SectionParser.PARA_TYPE_SECTION
            elif re.findall(pattern_level_2, paragraph):
                print("Came to LEVEL_1 pattern (1) , (2)")
                return SectionParser.PARA_TYPE_SECTION
            elif re.findall(pattern_level_3, paragraph):
                return SectionParser.PARA_TYPE_ERROR
            elif paragraph:
                print("Came to LEVEL_1 paragraph")
                return SectionParser.PARA_TYPE_PARA
            else:
                return SectionParser.PARA_TYPE_ERROR
        elif self.level == SectionParser.LEVEL_2:
            print("Came to LEVEL_2")
            if re.findall(pattern_level_1, paragraph):
                return SectionParser.PARA_TYPE_SECTION
            elif re.findall(pattern_level_2, paragraph):
                return SectionParser.PARA_TYPE_ERROR
            elif re.findall(pattern_level_3, paragraph):
                return SectionParser.PARA_TYPE_ERROR
            elif paragraph:
                print("Came to LEVEL_2 pattern paragraph")
                return SectionParser.PARA_TYPE_PARA
            else:
                return SectionParser.PARA_TYPE_ERROR
        else:
            return SectionParser.PARA_TYPE_ERROR

    def get_dict(self):
        child_dict_list = []
        for child in self.child_list:
            child_dict_list.append(child.get_dict())

        dictionary = {
            "level": self.level,
            "index": 0,
            "name": self.type_name,
            "paragraphs": child_dict_list
        }
        return dictionary

    def print_list(self):
        print(self.child_list)
