"""
License: CC0-1.0 (Public Domain)
"""

from io import StringIO
from unittest.mock import patch

import pytest

import elastic_pdf_index

@pytest.mark.parametrize("argument_values", [True, 1, 1.0])
def test_example(argument_values):
    assert True == argument_values

def test_get_usage():
    assert elastic_pdf_index.get_usage() == "elastic_pdf_index <wsdl_location>"

def test_print_hello():
    with patch('sys.stdout', new=StringIO()) as dummy_out:
        elastic_pdf_index.hello_world()
        assert dummy_out.getvalue() == "Hello World!\n"

