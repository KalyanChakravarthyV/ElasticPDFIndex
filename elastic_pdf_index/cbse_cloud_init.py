import sys
from lxml import etree



def parse_input_file(inputfile):
    chapters = []
    print()

    return  chapters


def index_pdfs(chapters, elastic_config):

    for chapter in chapters:
      print('Processing:' + chapter)


def main(inputfile, elastic_config):

    # download collection from mongodb
    chapters = parse_input_file(inputfile)

    # store news items in a csv file
    index_pdfs(chapters,elastic_config)


if __name__ == "__main__":
    # calling main function
    main(sys.argv, )
