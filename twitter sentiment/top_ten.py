import sys,json,re

terms = {}

def hw(tweet_file):
	for line in tweet_file:
		data = json.loads(line)
		if 'delete' not in data:
			hashList = data["entities"]["hashtags"]
			for hashTag in hashList:
				tag = hashTag["text"].encode("utf-8")
				if tag not in terms:
					terms[tag] = 1
				else:
					terms[tag] = terms[tag] + 1
	topTen = []
	count = 1
	for foo in sorted(terms, key=terms.get, reverse=True):
	    print foo, float(terms[foo])
	    if count < 10:
	    	count += 1
	    else:
	    	break
	  


def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
