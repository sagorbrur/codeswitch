from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer, AutoModelForSequenceClassification

class LanguageIdentification(object):
    def __init__(self, language):
        self.language = language
        if self.language == "spa-eng":
            print("Downloading pretrained model. It will take time according to model size and your internet speed")
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-spaeng-lid-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-spaeng-lid-lince")
            print("Model Download Completed!")
        elif self.language == "hin-eng":
            print("Downloading pretrained model. It will take time according to model size and your internet speed")
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-hineng-lid-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-hineng-lid-lince")
            print("Model Download Completed!")
        elif self.language == "nep-eng":
            print("Downloading pretrained model. It will take time according to model size and your internet speed")
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-nepeng-lid-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-nepeng-lid-lince")
            print("Model Download Completed!")
        else:
            raise Exception("No such language found! Try with spa-eng, hin-eng or  nep-eng with inverted comman like 'hin-eng' ")
            

    def identify(self, text):
        lid_model = pipeline('ner', model=self.model, tokenizer=self.tokenizer)
        results = lid_model(text)
        return results


class POS(object):
    def __init__(self, language):
        self.language = language
        if self.language == "spa-eng":
            print("Downloading pretrained model. It will take time according to model size and your internet speed")
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-spaeng-pos-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-spaeng-pos-lince")
            print("Model Download Completed!")
        elif self.language == "hin-eng":
            print("Downloading pretrained model. It will take time according to model size and your internet speed")
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-hineng-pos-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-hineng-pos-lince")
            print("Model Download Completed!")
        else:
            raise Exception("No such language found! Try with spa-eng, hin-eng or  nep-eng with inverted comman like 'hin-eng' ")
            

    def tag(self, text):
        pos_model = pipeline('ner', model=self.model, tokenizer=self.tokenizer)
        results = pos_model(text)
        return results


class NER(object):
    def __init__(self, language):
        self.language = language
        if self.language == "spa-eng":
            print("Downloading pretrained model. It will take time according to model size and your internet speed")
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-spaeng-ner-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-spaeng-ner-lince")
            print("Model Download Completed!")
        elif self.language == "hin-eng":
            print("Downloading pretrained model. It will take time according to model size and your internet speed")
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-hineng-ner-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-hineng-ner-lince")
            print("Model Download Completed!")
        else:
            raise Exception("No such language found! Try with spa-eng, hin-eng with inverted comman like 'hin-eng' ")
            

    def tag(self, text):
        pos_model = pipeline('ner', model=self.model, tokenizer=self.tokenizer)
        results = pos_model(text)
        return results


class SentimentAnalysis(object):
    def __init__(self, language):
        if language == "spa-eng":
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-spaeng-sentiment-analysis-lince")
            self.model = AutoModelForSequenceClassification.from_pretrained("sagorsarker/codeswitch-spaeng-sentiment-analysis-lince")
        else:
            raise Exception("No such language found! Try with spa-eng with inverted comman like 'spa-eng' ")
    def analyze(self, sentence):
        sa = pipeline('sentiment-analysis', model=self.model, tokenizer=self.tokenizer)
        result = sa(sentence)
        return result




