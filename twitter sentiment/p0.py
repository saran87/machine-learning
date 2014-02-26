import urllib,json

## Given a url, try to retrieve it. If it's text/html,
## print its base url and its text.
def getData(url):
  ufile = urllib.urlopen(url)  ## get file-like object for url
  info = ufile.info()   ## meta-info about the url content
  if info.gettype() == 'application/json':
   # print 'base url:' + ufile.geturl()
    data = json.loads(ufile.read())  ## read all its text
    return data


data =  getData("http://search.twitter.com/search.json?q=microsoft&page=2")
for result in data["results"]:
	print result["text"]

