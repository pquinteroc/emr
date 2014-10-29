# Experiments to Understand Training #

## Getting an Experimental Data Set ##

The input format tab-delimited file of the format:

    PhraseId        SentenceId      Phrase  Sentiment
    1       1       A series of escapades demonstrating the adage that what is good for the goose is also good for the gander , some of which occasionally amuses but none of which amounts to much of a story .    1
    32      1       good for the gander , some of which occasionally amuses but none of which amounts to much of a story    2

An example annotated traning set is the [Kaggle Movie Set Review Challenge](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews).  In this data set is:

  * train.tsv - an annotated training set
  * test.tsv - a test input file that is unannotated
  
## Generating Wordcounts ##

From your input data, you can use `wordcounts.py` to generate a file containing the word counts from any input data set (e.g., `train.tsv`).  The output is
one line for each word with the count of occurrences over the whole input data set.

## Training a Classifier ##

The classifier requires as input:

  * a list of stopwords (commas seperated)
  * a list of words (the output of wordcount.py will work)
  * a subset of feature words to use
  * the input training set
  * a filename to store the classifier
  
For example:

    python train.py stopwords.txt wordcounts.txt 1,250 train.tsv classifier-250.pickle
   
will train the model using the feature words of the first 250 words in wordcounts.txt

## Using a Classifier ##

You can test your classifier against the training data as follows:

    python test.py classifier-250.pickle stopwords.txt wordcounts.txt 1,250 train.tsv
   
This will output the incorrect classifications and a statistic for how many have been misclassified.

You can use the classifier by loading the stop words and loading your features:

    import stopwords,featureset
    
    stopWords = stopwords.load("stopwords.txt")
    featureWords = featureset.load("wordcounts.txt",1,250)

making a feature extractor:

    extractFeatures = featureset.makeExtractor(featureWords)
    
and running the classifier:

    f = open("classifier-250.pickle","rb")
    classifier = pickle.load(f)
    f.close()

    wordlist = [e.lower() for e in nltk.word_tokenize("this movie was awful") if len(e) >= 3 and not e.lower() in stopWords]
    c = int(classifier.classify(extractFeatures(wordlist)))
