import urllib.request, json

def __main__():
	url = "http://www.tevd.nl:81/groupedviewdata/"
	fileNames = getNames(url)
	i = 1
	amount = len(fileNames)
	for name in fileNames:	
		print("[{0}/{1}] {2}".format(str(i).zfill(3), str(amount).zfill(3), name + " " * 16), end="\r")
		getJSON(url, name)
		i = i + 1
	print("[{0}/{0}] Finished downloading teampage data".format(str(amount).zfill(3)))

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
	with open('data/teams/{0}'.format(name), 'wb') as f:
		f.write(jsonFile)


if __name__ == '__main__':
	__main__()
