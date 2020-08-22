from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer



class LanguageIdentification(object):
    def __init__(self, language):
        self.language = language
        if self.language == "spa-eng":
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-spaeng-lid-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-spaeng-lid-lince")
        elif self.language == "hin-eng":
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-hineng-lid-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-hineng-lid-lince")
        elif self.language == "nep-eng":
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-nepeng-lid-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-nepeng-lid-lince")
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
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-spaeng-pos-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-spaeng-pos-lince")
        elif self.language == "hin-eng":
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-hineng-pos-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-hineng-pos-lince")
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
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-spaeng-ner-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-spaeng-ner-lince")
        elif self.language == "hin-eng":
            self.tokenizer = AutoTokenizer.from_pretrained("sagorsarker/codeswitch-hineng-ner-lince")
            self.model = AutoModelForTokenClassification.from_pretrained("sagorsarker/codeswitch-hineng-ner-lince")
        else:
            raise Exception("No such language found! Try with spa-eng, hin-eng with inverted comman like 'hin-eng' ")
            

    def tag(self, text):
        pos_model = pipeline('ner', model=self.model, tokenizer=self.tokenizer)
        results = pos_model(text)
        return results



