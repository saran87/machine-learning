import sys,json,re

scores = {} # initialize an empty dictionary

def loadScores(sent_file):
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.

def getTweetScore(tweet):
	words = re.split("[^A-Za-z,']", tweet)
	score = 0
	for word in words:
		if word not in '':
			if word in scores:
				score = scores[word] + score
	return score

def hw(sent_file,tweet_file):
	
	happyState = {}
	loadScores(sent_file)
	max = -sys.maxint - 1;
	topState = ""

	states = ['IA', 'KS', 'UT', 'VA', 'NC', 'NE', 'SD', 'AL', 'ID', 'FM', 'DE', 'AK', 'CT', 'PR', 'NM', 'MS', 'PW', 'CO', 'NJ', 'FL', 'MN', 'VI', 'NV', 'AZ', 'WI', 'ND', 'PA', 'OK', 'KY', 'RI', 'NH', 'MO', 'ME', 'VT', 'GA', 'GU', 'AS', 'NY', 'CA', 'HI', 'IL', 'TN', 'MA', 'OH', 'MD', 'MI', 'WY', 'WA', 'OR', 'MH', 'SC', 'IN', 'LA', 'MP', 'DC', 'MT', 'AR', 'WV', 'TX']
	regex = re.compile(r'\b(' + '|'.join(states) + r')\b', re.IGNORECASE)

	for line in tweet_file:
		data = json.loads(line)
		if "text" in data:
			tweet = data["text"]
			tweet = tweet.lower()
			tweet = tweet.encode("utf-8")
			location = data["user"]["location"].encode("utf-8")
			lang =  data["user"]["lang"].encode("utf-8")
			if location not in '':
				if lang in 'en':
					match = regex.search(location)
					if match:
						score = getTweetScore(tweet)
						if match.group().upper() not in happyState:
							happyState[match.group().upper()] = score
						else:
							score = score + happyState[match.group().upper()]
							happyState[match.group().upper()] = score
						if score > max:
							max = score
							topState = match.group().upper()
	print topState

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
