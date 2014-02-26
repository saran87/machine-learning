import sys,json,re

scores = {} # initialize an empty dictionary

def loadScores(sent_file):
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.

def getTweetScore(tweet):
	words = tweet.split()
	score = 0
	for word in words:
		match = re.search("\w+",word)
		if match:
			if match.group().lower() in scores:
				score = scores[match.group().lower()] + score
	return score



def hw(sent_file,tweet_file):
	loadScores(sent_file)
	for line in tweet_file:
		data = json.loads(line)
		if "text" in data:
			tweet = data["text"]
			score = getTweetScore(tweet)
			print score
		else:
			print 0
			pass

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
