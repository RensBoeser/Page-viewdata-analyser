import os, json

def __main__():
	jsonFiles = list(map(lambda item: 'data/raw/' + item, os.listdir('data/raw')))
	data = lambda f: json.load(open(f))
	teams = getTeamNames(getDataList(data(jsonFiles[0])))

	teamData = list()
	for jsonFile in jsonFiles:
		date     = getDate(data(jsonFile))
		pageData = getDataList(data(jsonFile))
		for team in teams:
			teamData.append(getTeamData(pageData, team, date))

	teamResults = list()
	for team in teams:
		teamResult = list(filter(lambda item: item['teamName'] == team, teamData))
		teamResult = list(map(lambda item: removekey(item, 'teamName'), teamResult))
		count = len(teamResult)

		teamResults.append(dict(
			teamName = team,
			count    = count,
			data     = teamResult
		))

	for teamResult in teamResults:
		with open('data/teams/{0}.json'.format(teamResult['teamName'].replace(' ', '_')), 'w') as f:
			json.dump(teamResult, f)

def removekey(d, key):
    res = dict(d)
    del res[key]
    return res

def getTeamNames(data):
	teamResults = list()
	for item in data:
		team = item['team']
		if team not in teamResults:
			teamResults.append(team)
	return teamResults

def getDate(jsonFile):
	return jsonFile['datetime'].split(' ')[0]

def getDataList(jsonFile):
	return jsonFile['viewdata']

def getTeamData(data, teamName, date):
	pageData = list(map(lambda item: dict(pageName=item['subpage'], views=item['views']), filter(lambda item: item['team'] == teamName, data)))
	pageAmount = len(pageData)
	totalViews = sum(map(lambda item: item['views'], pageData))

	return dict(
		pageAmount = pageAmount,
		totalViews = totalViews,
		pageData   = pageData,
		teamName   = teamName,
		date       = date
	)


if __name__ == '__main__':
	__main__()
