import spacy

# Load the trained model
nlp = spacy.load("output_model")

def extract_entities(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        if ent.label_ in ["From", "To", "Datetime"]:
            entities.append((ent.text, ent.label_))
    return entities

# Example usage
text = "I want to make a flight from beautiful and nice Moscow to Chicago on 21st September 2024."
entities = extract_entities(text)
for entity in entities:
    print(f"Entity: {entity[0]}, Label: {entity[1]}")
