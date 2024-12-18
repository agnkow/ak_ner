from setuptools import setup

setup(
    name='ak_ner',
    version='0.1',
    description='Python package for NER (polish language)',
    author='agak',
    author_email='',
    include_package_data=True,
    packages=['ak_ner'],
    package_data={
        'ak_ner': ['sample_data/*.txt', 'sample_data/*.csv']
    },
    install_requires=[
        'pandas>=2.2.2',
        'spacy>=3.8.3'
    ]
)

