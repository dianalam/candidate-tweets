# investigating twitter strategies of the 2016 presidential candidates
A project to assess the social media strategies and performance of the 2016 presidential candidates (Clinton, Cruz, Rubio, Sanders, Trump) by using NLP techniques on candidate tweets. Utilizes tf-idf weighting, k-means clustering, topic modeling/LDA, and pyLDAvis to determine key topics and trends in topics over time, across party lines, and amongst the individual candidates. Also utilizes vaderSentiment, pattern, and textblob for sentiment and mood analysis of text. Visualization using d3.js and jQuery. 

For more information, see [my blog post](http://dianalam.github.io/2016/03/06/candidate-tweets.html). 
For the final interactive viz and to explore the results yourself, see [this page](http://dianalam.github.io/assets/tweets.html).

## in this repo
* `pull-tweets.py` python script that pulls candidate tweets 
* `tweets-analysis.ipynb` jupyter notebook with scripts and outputs for text processing, k-means clustering and topic modeling
* `viz/` contains data and script for interactive viz
* `presentation/` contains pdf presentation of findings & recommendations

## installation
### clone this repo  
```bash
$ git clone https://github.com/dianalam/candidate-tweets.git
```

### dependencies
Scripts were written in Python 2.7. You'll need the following modules: 
```bash
matplotlib >= 1.5.1  
nltk >= 3.1
numpy >= 1.10.1  
pandas >= 0.17.1  
python-dateutil >= 2.4.2
scipy >= 0.16.0
seaborn >= 0.6.0
sklearn >= 0.17
spacy >= 0.100
statsmodels >= 0.6.1
pattern >= 2.6
vaderSentiment 
```

To install modules, run:  
```bash
$ pip install <module>
```

### running
To run `pull-tweets.py` you'll need to save a `.twitter_config` file in your home directory with your Twitter credentials (consumer key, consumer secret, access token, access token secret). You'll also need mongoDB installed locally to store tweets (alternatively, edit the file to print/pickle results as desired instead of storing in mongoDB). Once that's done, run:
```bash
python pull-tweets.py
```

To open jupyter notebooks:
```bash
jupyter notebook 
```

To run visualizations:
```bash
python -m SimpleHTTPServer
```
Then navigate to instantiated port. Note that data files are static and will need to be regenerated if pulling new tweets. Stay tuned for an integrated database solution that will automatically update the viz! 

## data sources/other credits
Thanks to: 
* [Twitter REST API](https://www.yelp.com/dataset_challenge)
* [vaderSentiment](https://github.com/cjhutto/vaderSentiment)

