import spacy
from spacy.training.example import Example
from dataset import TRAINING_DATA

nlp = spacy.blank("en")

if 'ner' not in nlp.pipe_names :
    ner = nlp.create_pipe('ner')
    nlp.add_pipe('ner', last=True)
else :
    ner = nlp.get_pipe("ner")

for _, annotations in TRAINING_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

other_pipe = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
optimizer = nlp.begin_training()

for itn in range(10):
    for text, annotations in TRAINING_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], sgd=optimizer)

# Сохранение модели в директорию "model"
nlp.to_disk("output_model")