from lib.DocIterator import DocIterator
from lib.SectionParser import SectionParser

text_line = " 1. (1) This Act may be cited as the Coronavirus Disease 2019 (COVID -19) (Temporary Provisions) " \
                "Act, No.17 of 2021. The provisions of this Act shall be in operation for a period of two " \
                "years commencing from March 1, 2020."


def do_work():
    DocIterator.split_to_paragraph("09_test_reader.pdf")
    doc_iterator = DocIterator()
    doc_iterator.peek_word(0, "")


    #doc_iterator.print_list()
    doc_parser = SectionParser(doc_iterator)
    print(doc_parser.get_dict())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    do_work()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
