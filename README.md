# Code Switch
[![Documentation Status](https://readthedocs.org/projects/codeswitch/badge/?version=latest)](https://codeswitch.readthedocs.io/en/latest/?badge=latest)
[![PyPI Version](https://img.shields.io/pypi/v/codeswitch)](https://pypi.org/project/codeswitch/)

**CodeSwitch** is a NLP tool, can use for language identification, pos tagging, name entity recognition, sentiment analysis of code mixed data.

## Supported Code-Mixed Language
We used [LinCE](https://ritual.uh.edu/lince/home) dataset for training **multilingual BERT** model using huggingface [transformers](https://github.com/huggingface/transformers). `LinCE` has four language mixed data. We took three of it `spanish-english`, `hindi-english` and `nepali-english`. Hope we will train and add other language and task too.

* Spanish-English(spa-eng)
* Hindi-English(hin-eng)
* Nepali-English(nep-eng)

### Language Code
* `spa-eng` for spanish-english
* `hin-eng` for hindi-english
* `nep-eng` for nepali-english

## Installation
```
pip install codeswitch
```
## Dependency
* pytorch >=1.6.0

## Training Details
* All three(lid, ner, pos) sequence tagging model was trainend with huggingface [token classification](https://github.com/huggingface/transformers/tree/master/examples/token-classification)
* Sentiment Analysis Model trained with huggingface [text classification](https://github.com/huggingface/transformers/tree/master/examples/text-classification)
* You can find every model and evaluation results [here](https://huggingface.co/sagorsarker)

## Features & Supported Language
* Language Identification
  - spanish-english
  - hindi-english
  - nepali-english
* POS
  - spanish-english
  - hindi-english
* NER
  - spanish-english
  - hindi-english
* Sentiment Analysis
  - spanish-english

## Language Identification

```py
from codeswitch.codeswitch import LanguageIdentification
lid = LanguageIdentification('spa-eng') 
# for hindi-english use 'hin-eng', 
# for nepali-english use 'nep-eng'
text = "" # your code-mixed sentence 
result = lid.identify(text)
print(result)
```

## POS Tagging
```py
from codeswitch.codeswitch import POS
pos = POS('spa-eng')
# for hindi-english use 'hin-eng'
text = "" # your mixed sentence 
result = pos.tag(text)
print(result)

```


## NER Tagging
```py
from codeswitch.codeswitch import NER
ner = NER('spa-eng')
# for hindi-english use 'hin-eng'
text = "" # your mixed sentence 
result = ner.tag(text)
print(result)

```

## Sentiment Analysis

```py
from codeswitch.codeswitch import SentimentAnalysis
sa = SentimentAnalysis('spa-eng')
sentence = "El perro le ladraba a La Gatita .. .. lol #teamlagatita en las playas de Key Biscayne este Memorial day"
result = sa.analyze(sentence)
print(result)
# [{'label': 'LABEL_1', 'score': 0.9587041735649109}]


```

## Acknowledgement
* [LinCE](https://ritual.uh.edu/lince/home)
* [BERT](https://arxiv.org/abs/1810.04805)
* [huggingface](https://github.com/huggingface)




