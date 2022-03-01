from lib.DocIterator import DocIterator


class ParserBase:

    # def parse_doc(self, doc_iterator : DocIterator):
    #    raise NotImplementedError('You need to define a speak method!')
    def __init__(self) -> None:
        pass

    def get_dict(self):
        raise NotImplementedError('You need to define a speak method!')

