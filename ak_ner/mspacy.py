""" spaCy's NER model """

import pandas as pd
import spacy


def extract_ner_spacy(
        doc
        ,model
        ,type_out='df'
        ,col_text='text'
        ,col_id_doc='index'
):
    """
    Main function returning NER (using spacy model)
    for data in format: string or dataframe.

    :param doc: str or pd.DataFrame; input data
    :param model: str; spacy model name
    :param type_out: str; format for output data, ('list' or 'df'). Default is 'df'
    :param col_text: str; name of the column with the text variable
    :param col_id_doc: str; name of the column with the document number
    :return: list of tuples or pd.DataFrame; recognized entities, lemmas, NER labels
    """

    if isinstance(doc, str):
        ner_model = spacy.load(model)
        df_entities = extract_ner_from_txt(
            doc, ner_model, type_out
        )

    elif isinstance(doc, pd.DataFrame):
        ner_model = spacy.load(model)
        df_entities = extract_ner_from_df(
            doc, ner_model, type_out, col_text, col_id_doc
        )

    else:
        raise TypeError('Input data must be a string or a pd.DataFrame')
    return df_entities


def extract_ner_from_txt(
        doc_txt
        ,ner_model
        ,output_format='df'
):
    """
    Helper function to extract NER from a text string.

    :param doc_txt: str; input text for NER
    :param ner_model: spaCy model
    :param output_format: str; format for output data ('list' or 'df'). Default is 'df'
    :return: list of tuples or pd.DataFrame; recognized entities, lemmas, and NER labels
    """

    # NER recognition
    doc = ner_model(doc_txt)
    entities = [(e.text, e.lemma_, e.label_) for e in doc.ents]

    # Changing the format of returned data to a pd.DataFrame (if required)
    col_names = ['identified', 'lemma', 'entity']
    entities_out = correct_format_output(entities, output_format, col_names)
    return entities_out


def extract_ner_from_df(
        doc_df
        ,ner_model
        ,output_format='df'
        ,col_text='text'
        ,col_id_doc='index'
):
    """
    Helper function to extract NER from a DataFrame.

    :param doc_df: pd.DataFrame; input DataFrame containing text for NER
    :param ner_model: spaCy model
    :param output_format: str; format for output data ('list' or 'df'). Default is 'df'
    :param col_text: str; name of the column with the text variable
    :param col_id_doc: str; name of the column with the document number
    :return: list of tuples or pd.DataFrame; recognized entities, lemmas, and NER labels
    """

    docs = doc_df[col_text].to_list()
    ids = doc_df[col_id_doc].to_list()
    entities_all =[]
    for i, doc_i in enumerate(docs):
        doc = ner_model(doc_i)
        entities = [(ids[i], e.text, e.lemma_, e.label_) for e in doc.ents]
        entities_all = [*entities_all, *entities]

    # Changing the format of returned data to a pd.DataFrame (if required)
    col_names=['id_doc', 'identified', 'lemma', 'entity']
    entities_out = correct_format_output(entities_all, output_format, col_names)
    return entities_out


def correct_format_output(
        entities
        ,output_format
        ,col_name
):
    """
    Helper function to format output as either a list of tuples or DataFrame.

    :param entities: list of tuples; extracted entities with lemmas and labels
    :param output_format: str; 'list' or 'df' indicating desired output format
    :param col_name: list of str; column names for DataFrame output
    :return: list of tuples or pd.DataFrame; formatted entities
    """

    if output_format == 'list':
        return entities
    elif output_format== 'df':
        return pd.DataFrame(entities, columns=col_name)
    else:
        raise ValueError('output_format should be "list" or "df"')

