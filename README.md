# Korean Text Mining 
This program is developed using Python and KoNLPy as text mining library.
[KoNLPy](http://konlpy.org/en/latest/) is a Python package for natural language processing (NLP) of the Korean language. 

## Text Mining Process
1. Data Collection
    + Newspaper: [Joongang Ilbo](https://joongang.joins.com/) 
    + Web Scrapping: Using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. Data Preprocessing
    + Tokenization
3. Data Representation
    + Word2Vec
    + PCA Plot
4. Data Analysis

## Prerequisites
+ Download and Install [Python](https://www.python.org/downloads/) on your workstation
+ Install [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library
+ Install requests module using ``pip install request``
+ Install [KoNLPy](http://konlpy.org/en/latest/install/)
+ Install related libraries (matplotlib, gensim, nltk)

## Source Code Description
+ ``joongang.py`` - web scrapping
+ ``morph.py`` - morphing code, such as word2vec
+ ``joongang.txt`` - result file from scrapping

## Results
Following is the result of the most similar word to 금융 or finance word in Korean
```
등
0.954851508140564
중앙
0.9336299300193787
것
0.9300297498703003
한국
0.9291011691093445
검사
0.9279869198799133
형사
0.9176149368286133
일본
0.9146363735198975
시장
0.9116146564483643
조치
0.9072641134262085
기업
0.8989660739898682
```

### notes
Originally I developed the program on Mac OS, but I have tried to run also on Windows OS. And work well by changing several line of code, especially the file location.

