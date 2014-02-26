import sys,json,re

terms = {} # initialize an empty dictionary

def countTerms(tweet):
	words = re.split("[^A-Za-z,]", tweet)
	count = 0
	filteredList = []
	for word in words:
		if word is not '':
			if word in terms:
				terms[word] = terms[word] + 1
			else:
				terms[word] = 1
			count += 1

	return count



def hw(tweet_file):
	total = 0
	for line in tweet_file:
		data = json.loads(line)
		if "text" in data:
			tweet = data["text"]
			tweet = tweet.encode("utf-8")
			tweet = re.sub(r"https?://","", tweet)
			#tweet = re.sub(r"[-\./,)=()?!:&\";]"," ", tweet)
			total += countTerms(tweet)
	for term in terms:
		count = terms[term]
		print "%s\t%f" % (term, float(count)/float(total))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
