from lib.DocIterator import DocIterator
from lib.SectionParser import SectionParser
import json

text_line = " 1. (1) This Act may be cited as the Coronavirus Disease 2019 (COVID -19) (Temporary Provisions) " \
                "Act, No.17 of 2021. The provisions of this Act shall be in operation for a period of two " \
                "years commencing from March 1, 2020."


def do_work():
    doc_iterator = DocIterator("1.pdf")
    doc_parser = SectionParser(doc_iterator, "body")
    json_object = json.dumps(doc_parser.get_dict(), indent=4)

    folder_name = f'test.json'
    with open(folder_name, "w") as outfile:
        outfile.write(json_object)
        print("json file -" + folder_name + " was created.")
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    do_work()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
