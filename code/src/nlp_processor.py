import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

def process_text(text):
    """Process the input text and return a list of tokens."""
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens

def get_noun_chunks(text):
    """Process the input text and return a list of noun chunks."""
    doc = nlp(text)
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    return noun_chunks

def get_entities(text):
    """Process the input text and return a list of named entities."""
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def get_pos_tags(text):
    """Process the input text and return a list of part-of-speech tags."""
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags
