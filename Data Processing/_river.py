import nltk,string
from pymongo import MongoClient
from operator import itemgetter
from sklearn.feature_extraction.text import TfidfVectorizer
import math

server = 'ds049436.mlab.com:49436'
port = 41939
db_name = 'nlp_team'
username = 'nlp'
password = 'nlp'

# connect to server
conn = MongoClient(server, port)

# Get the database
db = conn[db_name]

# Have to authenticate to get access
db.authenticate(username, password)

cur=db.river.find()

list_query =[]
dict_collections={}
dict_collections['mt'] = 'mountain'
dict_collections['mountain'] = 'mountain'
dict_collections['city'] = 'cities'
dict_collections['cities'] = 'cities'
dict_collections['state'] = 'state'
dict_collections['st'] = 'state'
dict_collections['lake'] = 'lake'
dict_collections['river'] = 'river'
dict_collections['rivers'] = 'river'

long_river=-10000
short_river=10000

stateRiver={}

riv_long=[]
riv_short=[]
river_sent=[]
for i in cur:
    if int(i["length"])> int(long_river):
        long_river=i["length"]
        riv_long=i["name"]
    if int(i["length"]) <int(short_river):
        short_river=i["length"]
        riv_short=i["name"]

    riverlist = set()
    for r in i["states"]:
        r=r.replace("]","")
        r=r.replace("[","")
        riverlist.add(r)
    # print(riverlist)
    stateRiver[i["name"]] = riverlist

    river_sent.append("The length of the river "+i["name"].title()+" is "+i["length"]+" meters")
    u=i["states"]
    m=set()
    for t in u:
        print(t)
        t=t.replace("[","")
        t=t.replace("]","")
        m.add(t.title())
    river_sent.append("The river "+i["name"].title()+" flows through the states "+" , ".join(m))
    river_sent.append("The river "+i["name"].title()+" flows through "+ str(len(i["states"]))+" states")

# for st,riv in stateRiver.items():
#     print("The rivers that flow in the state "+st +" are "+",".join(riv))
print("*********************")
# print(stateRiver)
print("******************")
for st , rv in stateRiver.items():
        river_sent.append("The river that flows through the states " +" , ".join(rv).title() +" is "+st.title())

river_sent.append("The length of the longest river in USA is "+long_river+" meters")
river_sent.append("The longest river in USA is "+riv_long)
river_sent.append("The length of the shortest river in USA is " + short_river+" meters")
river_sent.append("The shortest river in USA is "+riv_short)
db.questions.insert({'river': river_sent})

print("--------------")
# print(sorted(cos.items(), key=itemgetter(1),reverse=True))
# print("shory river"+long_river+"is "+riv_short)