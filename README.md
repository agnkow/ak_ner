# ak_ner

Biblioteka z modelami NER (język polski)
```
pip install git+https://github.com/agnkow/ak_ner.git@master
```
```
import ak_ner
```
<br/>

## spaCy

<details>
    <summary>
        <font size="3">
            Info o bibliotece spaCy 
        </font>
    </summary>
<br />

**Oficjalne modele spaCy:**
* pl_core_news_sm
* pl_core_news_md
* pl_core_news_lg

**Pobranie modeli:**
```
python -m spacy download pl_core_news_sm
python -m spacy download pl_core_news_md
python -m spacy download pl_core_news_lg
```

**Dokumentacja biblioteki spaCy:**
https://spacy.io/models/pl

</details>


<details>
    <summary>
        <font size="3">
            extract_ner_spacy()
        </font>
    </summary>
<br />

**extract_ner_spacy()** - funkcja zwracajaca rozpoznane 
jednostki nazewnicze dla danych wejściowych w formacie 
*string* lub *pd.DataFrame*. 
Dane wyjściowe: rozpoznane frazy, lematy, 
etykiety jednstek nazewniczych możemy otrzymać
w formie listy zawierającej tuple lub w formacie pd.DataFrame.

```
extract_ner_spacy(
        doc
        ,model
        ,type_out='df'
        ,col_text='text'
        ,col_id_doc='index'
)
```

Parametry:
* ***doc:** string or pd.DataFrame;* dane wejściowe
* ***model:** string;* nazwa modelu spacy
* ***type_out:** string;* format danych wyjściowych ('list' lub 'df'). Wartość domyślna: 'df'.
Oznaczenia: 'df' - pd.DataFrame, 'list' - lista zawierająca tuple.
* ***col_text:** string;* nazwa kolumny zawierającej dane tekstowe
* ***col_id_doc:** string;* nazwa kolumny zawierającej numer dokumentu 
(dotyczy danych wejściowych w formacie *pd.DataFrame*)

Przykład:
```
import ak_ner

data_cire = ak_ner.read_example('str')
cire_ner = ak_ner.extract_ner_spacy(data_cire, model='pl_core_news_sm')

print(cire_ner.tail(3))
```
```
     id_doc identified     lemma    entity
132       4   Gazpromu   Gazprom   orgName
133       4     Czeban    Czeban  persName
134       4   listopad  listopad      date```
```
</details>
<br/>

## Przykładowe dane

<details>
    <summary>
        <font size="3">
            read_example()
        </font>
    </summary>
<br />

**read_example()** - funkcja wczytująca przykładowe dane.
Dane są dostępne w formacie *string* lub *pd.DataFrame*.

```
read_example(format_example='df')
```

Parametry:
* ***format_example:** string;* format danych,
do wyboru: *'df' (pd.DataFrame)*, *'str' (string)*; 
domyślnie: *'df'*.

Przykład:
```
data_txt = read_example(format_example='str')
data_df = read_example(format_example='df')

print(data_txt[:105])
```
```
Komisja Europejska poinformowała w środę, że zatwierdziła, zgodnie z unijnymi zasadami pomocy publicznej,
```
```
print(data_df.head(2))
```
```
   index         text_date                                                url  \
0      0  2021-11-24 10:00  https://rynek-gazu.cire.pl/artykuly/serwis-inf...   
1      1  2021-11-23 21:00  https://rynek-gazu.cire.pl/artykuly/serwis-inf...   

                                                text  
0  Górnośląsko-Zagłębiowska Metropolia ma ofertę ...  
1  Nord Stream 2 wspiera fundacja klimatyczna z M...  
```

Przykładowe dane zawarte w bibliotece **ak_ner** pochodzą z portalu: 
https://www.cire.pl/

</details>
<br>

*Więcej modeli wkrótce* &#128540;
