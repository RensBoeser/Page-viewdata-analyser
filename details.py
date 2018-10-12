import json
# HOW THE JSON DATA LOOKS:
# data: [
#		{ 
#			totalViews: number, 
#			date: string, 
#			pageData: [
#				{
#					pageName: string, 
#					views: number
#				} 
#			] 
#		} 
# ]

def __main__():
	teamName = input("team: ").lower()
	data = teamData(teamName)

	print(pageNames(data))
	page = input("(empty for total) page: ").lower()

	if page == "":
		viewdata = totalViews(data)
	else:
		viewdata = totalPageViews(data, page)
		if len(viewdata) == 0:
			print('page not found')

	for datapoint in viewdata:
		last = viewdata[viewdata.index(datapoint) - 1] if viewdata.index(datapoint) - 1 >= 0 else datapoint
		difference = datapoint['views'] - last['views']
		print('{0} | {1} | {3}{2}'.format(datapoint['date'], datapoint['views'], difference, "+" if difference > 0 else ""))
	
def teamData(teamName):
	with open('./data/teams/{0}.json'.format(teamName)) as f:
		return sorted(json.loads(f.read())['data'], key=lambda k: k['date'])

def pageNames(teamData):
	result = []
	for page in teamData[-1]['pageData']:
		result.append(page['pageName'].lower())
	return result

def totalViews(teamData):
	result = []
	for data in teamData:
		result.append(
			dict(date = data['date'], views = data['totalViews'])
		)
	return result

def totalPageViews(teamData, page):
	result = []
	for data in teamData:
		pageData = list(filter(lambda k: k['pageName'].lower() == page, data['pageData']))
		if len(pageData):
			result.append(
				dict(date = data['date'], views = pageData[0]['views'])
			)
	return result


if __name__ == '__main__':
	__main__()
