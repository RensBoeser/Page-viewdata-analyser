import urllib.request, json

def __main__():
	url = "http://tevd.nl:81"
	fileNames = getNames(url)
	for name in fileNames:
		getJSON(url, name)

def getPage(url):
	result = urllib.request.urlopen(url).read()
	return result

def getNames(url):
	content = str(getPage(url))
	result = list()

	i = content.find('.json">')
	while i != -1:
		content = content[i+7:]
		result.append(content[:content.find('</a>')])
		i = content.find('.json">')
	return result

def getJSON(url, name):
	jsonFile = getPage(url + "/" + name)
	with open('data/raw/{0}'.format(name), 'wb') as f:
		f.write(jsonFile)


if __name__ == '__main__':
	__main__()
