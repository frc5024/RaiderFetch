import requests
import feedparser

class Fetcher(object):
	"""(optional) Pass in a github account"""
	def __init__(self, account="frc5024"):
		self.account = str(account)
		self.feed = None
	
	## PUBLIC ##
	
	def fetch(self):
		self.feed = feedparser.parse("https://github.com/" + self.account + ".atom")
	
	def getFeed(self):
		output = []
		for entry in self.feed.entries:
			output.append(self.__toReadable(entry))
		return output
	
	def getMembers(self):
		"""Gets all public members"""
		memberlist = requests.get("https://api.github.com/orgs/"+ self.account +"/members").json()
		output = []
		for account in memberlist:
			output.append({"username":account["login"], "avatar":account["avatar_url"], "url":account["html_url"]})
		return output
	
	def isMember(self, username: str):
		if str(requests.get("https://api.github.com/orgs/"+ self.account +"/members/" + username)) == "<Response [204]>":
			return True
		else:
			return False
	
	def getRepos(self):
		"""Get all public repos"""
		repolist = requests.get("https://api.github.com/orgs/"+ self.account +"/repos").json()
		output = []
		for repo in repolist:
			output.append({"name":repo["name"], "full_name":repo["full_name"], "description":repo["description"], "url":repo["html_url"],  "ssh_url":repo["ssh_url"], "id":str(repo["id"]), "default_branch":repo["default_branch"], "language":str(repo["language"]), "counts":{"forks":repo["forks_count"], "stars":repo["stargazers_count"], "watchers":repo["watchers_count"],"size":repo["size"], "issues":repo["open_issues_count"]} })
		return output
	
	## PRIVATE ##
	
	def __getEntry(self, entry):
		return(self.feed.entries[entry])
	
	def __toReadable(self, entry):
		return {"link":entry["link"], "time":entry["updated"], "title":entry["title"]}

## DEBUG ##
# rf = Fetcher()
# # rf.fetch()
# # print(rf.getFeed())
# print(rf.getMembers())
# print(rf.isMember("ewpratten"))
# print(rf.getRepos())