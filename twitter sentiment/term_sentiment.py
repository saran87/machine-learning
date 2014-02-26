import sys,json,re

scores = {} # initialize an empty dictionary
terms = {}

def loadScores(sent_file):
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.

def calTweetScore(tweet):
	words = re.split("[^A-Za-z,']", tweet)
	score = 0
	filteredList = []
	for word in words:
		if word not in '':
			if word in scores:
				score = scores[word] + score
			elif word in terms:
				terms[word][1] = terms[word][1] + 1
			else:
				terms[word] = [0,1]
				filteredList.append(word)
	
	for word in filteredList:
		terms[word][0] = terms[word][0] + score
		terms[word][1] = terms[word][1] + 1



def hw(sent_file,tweet_file):
	loadScores(sent_file)
	for line in tweet_file:
		data = json.loads(line)
		if "text" in data:
			tweet = data["text"]
			tweet = tweet.lower()
			tweet = tweet.encode("utf-8")
			tweet = re.sub(r"https?://","", tweet)
			#tweet = re.sub(r"[-\./,)=()?!:\";]"," ", tweet)
			calTweetScore(tweet)
	for term in terms:
		count = 0
		total = 0
		word = terms[term]
		total = word[0] 
		count = word[1]
		if count > 0:
			print "%s\t%.3f" % (term, total/float(count))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
