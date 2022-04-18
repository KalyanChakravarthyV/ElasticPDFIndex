"""
License: CC0-1.0 (Public Domain)
"""

# from setuptools import setup, find_packages
#
with open('README.md') as _f:
    _README_MD = _f.read()

from setuptools import setup

_VERSION = '0.1'

setup(
    name='elastic_pdf_index',
    version=_VERSION,
    description='Index PDFs for full text search ',
    long_description=_README_MD,
    classifiers=[
    ],
    url='https://github.com/KalyanChakravarthyV/ElasticPDFIndex',
    download_url='https://github.com/KalyanChakravarthyV/ElasticPDFIndex/tarball/{}'.format(_VERSION),  # TODO.
    author='Kalyan Chakravarthy V',
    author_email='kalyan@vadlakonda.in',
    packages=['elastic_pdf_index'],
    test_suite="testing",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=[],
    include_package_data=True,
    license='License: CC0-1.0 (Public Domain)',
    keywords='WSDL ArrayTo',
    entry_points={
        'console_scripts': [
            'elastic_pdf_index=elastic_pdf_index:init'
        ]
    }
)
