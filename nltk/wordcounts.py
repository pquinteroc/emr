import sys
import nltk
import sets
import operator

inputFilename = sys.argv[1];
outputFilename = sys.argv[2];

stopWords = nltk.corpus.stopwords.words('english')
stemmer = nltk.stem.lancaster.LancasterStemmer()

words = {}

inputData = open(inputFilename,"r")
# skip first line
inputData.readline();

for line in inputData:
   parts = line.split("\t")
   for word in [e.lower() for e in nltk.word_tokenize(parts[2]) if len(e) >= 3 and not e.lower() in stopWords]:
      word = stemmer.stem(word)
      words[word] = words[word] + 1 if word in words else 1

inputData.close()

wordsSorted = sorted(words.items(), key=operator.itemgetter(1),reverse=True)

output = open(outputFilename,"w")
for w in wordsSorted:
   output.write("{0}\t{1}\n".format(w[0],w[1]))
output.close()
   
