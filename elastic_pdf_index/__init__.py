"""
License: CC0-1.0 (Public Domain)
"""
from elastic_pdf_index import cbse_cloud_init
import sys, getopt


def hello_world():
    print("Hello World!")


def printusage():
    print('elastic_pdf_index -i <inputfile> ')


def init():
    input_file  =  elastic_config = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:e:", ["input-file=", "elastic-config="])
    except getopt.GetoptError:
        printusage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            printusage()
            sys.exit(1)
        elif opt in ("-i", "--input-file"):
            input_file = arg
        elif opt in ("-e", "--elastic-config"):
            elastic_config = arg

    if elastic_config is None or input_file is None:
        printusage();
        sys.exit(1)

    cbse_cloud_init.main(input_file, elastic_config)


if __name__ == "__main__":
    init()
