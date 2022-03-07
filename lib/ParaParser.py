from lib.ParserBase import ParserBase
from lib.DocIterator import DocIterator


class ParaParser(ParserBase):

    def __init__(self, doc_iterator: DocIterator):
        self.text = ""
        self.text = doc_iterator.get_line()
        print("para line is- " + self.text)

    def get_dict(self):
        dictionary = {
            "text": self.text
        }
        return dictionary
