# exercise 1
import os


def write_to_file(text, output_file_path):
    if os.path.exists(output_file_path):
        raise RuntimeError("Output file already exists")
    with open(output_file_path, "w") as file:
        file.write(text)


text = input("Enter your text: ")
write_to_file(text, "output.txt")

# exercise 2
import spacy


nlp = spacy.load('en_core_web_sm')


def count_stopwords(input_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()
    doc = nlp(text)
    stop_words = nlp.Defaults.stop_words
    count = sum(1 for token in doc if token.text.lower() in stop_words)
    return count


count_stopwords("output.txt")
print(count_stopwords("output.txt"))

# exercise 3
def remove_stopwords(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()
    doc = nlp(text)
    stop_words = nlp.Defaults.stop_words
    filtered_words = [token.text for token in doc if not token.text.lower() in stop_words]
    filtered_text = ' '.join(filtered_words)
    with open(output_file_path, 'w') as file:
        file.write(filtered_text)


remove_stopwords("output.txt", "filtered.txt")

# exercise 4
def tokenize_text(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        text = file.read()
    doc = nlp(text)
    with open(output_file_path, 'w') as file:
        for token in doc:
            file.write(f"{token.text:{10}}\t{token.pos_:{10}}\t{token.dep_:{10}}\n")


tokenize_text("output.txt", "tokenized.txt")


# exercise 5
import spacy
from spacy import displacy


def save_visualization(input_file_path, output_file_path):
    with open(input_file_path, "r") as file:
        text = file.read().strip()
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    svg = displacy.render(doc, style="dep", jupyter=False)

    with open(output_file_path, "w") as file:
        file.write(svg)


save_visualization("output.txt", "visualization.svg")
