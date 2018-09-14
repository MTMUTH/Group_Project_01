
# coding: utf-8

# In[65]:


import requests
import json
url = "https://www.fantasyfootballnerd.com/service/draft-rankings/json/ysxhvrenrddf"
#url = "https://www.fantasyfootballnerd.com/service/players/json/ysxhvrenrddf/QB


# In[66]:


print(requests.get(url))


# In[67]:


URLRQB = "https://www.fantasyfootballnerd.com/service/weekly-rankings/json/ysxhvrenrddf/QB/"
URLRWR = "https://www.fantasyfootballnerd.com/service/weekly-rankings/json/ysxhvrenrddf/WR/"
URLRRB = "https://www.fantasyfootballnerd.com/service/weekly-rankings/json/ysxhvrenrddf/RB/"

DataRQB = {}
DataRWR = {}
DataRRB = {}

for i in range(1,17):
    URLTQB = URLRQB + str(i) + '/1/'
    URLTWR = URLRWR + str(i) + '/1/'
    URLTRB = URLRRB + str(i) + '/1/'
    
    DataTQB = requests.get(URLTQB).json()
    DataTWR = requests.get(URLTWR).json()
    DataTRB = requests.get(URLTRB).json()
    
    DataRQB['WK' + str(i)] = DataTQB
    DataRWR['WK' + str(i)] = DataTWR
    DataRRB['WK' + str(i)] = DataTRB

print(DataRQB)
print(DataRWR)
print(DataRRB)
    


# In[59]:


print(requests.get(url).json())
data = requests.get(url).json()


# In[60]:


response = requests.get(url).json()
print(json.dumps(response, indent=4, sort_keys=True))


# In[61]:


index = len(data['DraftRankings'])
# for i in range(index):
#    print(data['Players'][i]['displayName'])
# data["Players"][0]['displayName']


# In[62]:


#Initalizing dictionary for data storage
XQB = {'fname':[], 'lname':[], 'positionRank':[], 'position':[], 'displayName':[]}
XRB = {'fname':[], 'lname':[], 'positionRank':[], 'position':[], 'displayName':[]}
XWR = {'fname':[], 'lname':[], 'positionRank':[], 'position':[], 'displayName':[]}

for i in range(1,17):
    XQB['WK' + str(i)] = []
    XRB['WK' + str(i)] = []
    XWR['WK' + str(i)] = []


# In[63]:


for i in data['DraftRankings']:
    pos = i['position']
    if pos == 'QB':
        XQB['fname'].append(i['fname'])
        XQB['lname'].append(i['lname'])
        XQB['positionRank'].append(i['positionRank'])
        XQB['position'].append(i['position'])
        XQB['position'].append(i['position'])
        XQB['displayName'].append(i['displayName'])
    elif pos == 'WR':
        XWR['fname'].append(i['fname'])
        XWR['lname'].append(i['lname'])
        XWR['positionRank'].append(i['positionRank'])
        XWR['position'].append(i['position'])
        XWR['displayName'].append(i['displayName'])
    elif pos == 'RB':
        XRB['fname'].append(i['fname'])
        XRB['lname'].append(i['lname'])
        XRB['positionRank'].append(i['positionRank'])
        XRB['position'].append(i['position'])
        XRB['displayName'].append(i['displayName'])
        
print(XQB)
print(XWR)
print(XRB)


# In[64]:



            
for i in range(len(XRB['fname'])):
    name = XRB['displayName'][i]
    for j in range(1,17):
        key = 0
        for k in range(len(DataRRB['WK' + str(j)]['Rankings'])):
            name2 = DataRRB['WK' + str(j)]['Rankings'][k]['name']
            if name == name2:
                XRB['WK' + str(j)].append(DataRRB['WK' + str(j)]['Rankings'][k]['standard'])
                key = 1
                
        if key==0:
            XRB['WK' + str(j)].append(0.0)          


for i in range(len(XQB['fname'])):
    name = XQB['displayName'][i]
    for j in range(1,17):
        key = 0
        for k in range(len(DataRQB['WK' + str(j)]['Rankings'])):
            name2 = DataRQB['WK' + str(j)]['Rankings'][k]['name']
            if name == name2:
                XQB['WK' + str(j)].append(DataRQB['WK' + str(j)]['Rankings'][k]['standard'])
                key = 1
                
        if key==0:
            XQB['WK' + str(j)].append(0.0)
            
print(XQB)
print(XRB)
print(XWR)

