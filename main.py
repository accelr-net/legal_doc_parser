from lib.DocIterator import DocIterator
from lib.SectionParser import SectionParser
import json


def do_work():
    doc_iterator = DocIterator("11.pdf")
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
