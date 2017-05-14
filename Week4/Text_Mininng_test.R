library(tm)
library(wordcloud2)
# carrega o dataset do twitter
f = "/Users/Marku/Documents/data_center/WorkSpace/Social-Media-Data-Analytics/Week4/results_trump.csv"
twitter_data = read.table(file=f, header=TRUE,sep=",",encoding="UTF-8", stringsAsFactors = FALSE)
# remove o caracter 'b' do começo da string
twitter_data$text = paste(substr(twitter_data$text,2,nchar(twitter_data$text))) 

text = twitter_data$text
text_clean = gsub("(RT|via)((?:\\b\\W*@\\w+)+)", "", text)
text_clean = gsub("@\\w+", "", text_clean)
text_clean = gsub("[[:punct:]]", "", text_clean)
text_clean = gsub("[[:digit:]]", "", text_clean)
text_clean = gsub("http\\w+", "", text_clean)

text_corpus = Corpus(VectorSource(text_clean)) 

#text_corpus = tm_map(text_corpus, tolower)
#text_corpus = tm_map(text_corpus, removeWords, c(stopwords("english"), "is"))
#text_corpus = tm_map(text_corpus, stripWhitespace)
#text_corpus = tm_map(text_corpus, PlainTextDocument)

control = list(removePunctuation = TRUE,
               removeNumbers = TRUE, 
               wordLengths = c(1, Inf), weighting = weightBin,
               stopwords = c("and", "of", "for", "in", "a", "is", "the", "as", "to", "are", "have","with","you","if","was","by","could","this","over","has","that"))



tdm = TermDocumentMatrix(text_corpus,control)

# make word frequency
wordFreq <- sort(rowSums(as.matrix(tdm)), decreasing = TRUE)

# make word cloud
wordcloud(words = names(wordFreq), freq = wordFreq,
          min.freq = 2, random.order = F)

