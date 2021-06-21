# Key Terms Extraction
## About
Key term extraction, also known as keyword extraction, is an important Natural
Language Processing (NLP) task that makes it possible to automatically identify
terms that best describe the subject of a document.
Extracting keywords can help to get to the text meaning, and with splitting
texts into different categories. In this project,
we will extract relevant words from a collection of news stories.
There are many different ways to do it, but we will focus on frequencies,
*pos search* (part of speech search), and *TF-IDF* (term frequency-inverted document frequency)
methods. Each method can yield the
results with varying degrees of accuracy for different texts. In reality, it is
always good to try various methods and choose the best.
## Description
## Objectives
1. Most frequent words  
   Read a file containing news articles, lowercase the text, tokenize it with
   the NLTK tokenizer's help, and create a token frequency list. 
2. Text preprocessing pipeline  
   Improve the results by applying lemmatization and deleting stop-words,
   digits, and punctuation. 
3. Nouns are keywords  
   Discover how to use part-of-speech tagging to extract the most frequent nouns
   and refine your keywords.
4. Modifying frequencies for better results  
Find out how to identify words with the highest TF-IDF score.
5. Print each story's headline and the five most frequent words in descending order.