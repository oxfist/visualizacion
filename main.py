import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import RegexpTokenizer, WordPunctTokenizer

nltk.download("stopwords")

stemmer = SnowballStemmer("spanish")
stop_words = set(stopwords.words("spanish"))

tema = "Proyecto de acuerdo de los Honorables Senadores señor Chahuán, señoras Aravena, Ebensperger, Gatica, Órdenes y Sepúlveda, y señores Bianchi, Castro González, Castro Prieto, De Urresti, Durana, Edwards, Flores, Galilea, Huenchumilla, Keitel, Kusanovic, Kuschel, Latorre, Macaya, Moreira, Prohens, Pugh, Sandoval, Sanhueza y Walker, con el que solicitan a la señora Ministra del Interior y Seguridad Pública que, si lo tiene a bien, instruya la habilitación de controles policiales permanentes en los pasos fronterizos del país, durante las veinticuatro horas, tanto de días hábiles como feriados. (Boletín N° S 2.507-12). APROBADO."

numero_boletin = RegexpTokenizer(r"[Bb]olet[íi]n.*\d+").tokenize(tema)
numero_boletin = "".join(re.findall(r"[0-9-]+", numero_boletin[0]))

tokenized_tema = RegexpTokenizer(r"\w+").tokenize(tema)
tokenized_tema = WordPunctTokenizer().tokenize(" ".join(tokenized_tema))
tokenized_tema.append(numero_boletin)

stemmed_tema = [
    stemmer.stem(token) for token in tokenized_tema if token.lower() not in stop_words
]

stemmed_tema = list(filter(lambda w: len(w) > 1, stemmed_tema))

print(stemmed_tema)
