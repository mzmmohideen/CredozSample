import json

class my_dictionary(dict): 

    # __init__ function 
    def __init__(self): 
        self = dict() 

    # Function to add key:value 
    def add(self, key): 
        self[key] = [] 


userList = my_dictionary() 

with open('wikiPageAuthors.json') as json_file:
    articleData = json.load(json_file)

with open('ew_users.json') as json_file:
    userData = json.load(json_file)

# Summaries all the articles based on last editor username
for page in articleData['query']['pages']:
    pageTitle = page['title']

    for metatag in page['revisions']:
        pageAuthor = metatag['user']

    if pageAuthor in userList:
        userList[pageAuthor].append(pageTitle)
    else:
        userList.add(pageAuthor)
        userList[pageAuthor].append(pageTitle)

# Send an email to each user telling them which articles they last edited/need to review.

for key,val in userList.items():
    # Look up the user's email address
    userLookup = next(item for item in userData["data"] if item["user_name"] == key)
    toAddr = userLookup['user_email']
    print('userLookup', userLookup)