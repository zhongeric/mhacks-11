from audiototext import audio_text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# fill example_sent
def filter(audio_string):
    example_sent = audio_string
   

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(example_sent)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
 
  
    print(filtered_sentence)
