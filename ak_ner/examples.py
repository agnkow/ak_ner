import importlib.resources
import pandas as pd


def read_example(format_example='df'):
    """
    A function loading sample text data

    :param format_example: str, output data format ('df' or 'str')
    :return: str or pd.DataFrame, text data
    """

    if format_example == 'df':
        pl_df_path = (importlib.resources
                      .files('ak_ner.sample_data')
                      .joinpath('cire_sample.csv')
                      )
        pl_example = pd.read_csv(pl_df_path, sep=';')

    elif format_example == 'str':
        pl_example = (importlib.resources
                      .files('ak_ner.sample_data')
                      .joinpath('cire_sample.txt')
                      .read_text()
                      )
    return pl_example

