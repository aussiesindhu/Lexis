import nltk,string
from pymongo import MongoClient
import operator
from operator import itemgetter
from sklearn.feature_extraction.text import TfidfVectorizer

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

city_corpus =["City Birmingham has 284413 ppl","284413 ppl live in city Birmingham", "The population of city Birmingham is 284413",
              "City Birmingham is in the state Alabama",
              "State S has Y cities"," city x has the largest no of people ",
              "x is the most populates city",
              " x is the most populates state ", "least populates"," the state code for alabama is al"]
cur=db.cities.find()

# print(cur)

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

city={}

city_sent=[]
state_city={}
city_pop={}
for i in cur:
    cityList=set()
    if i["state"] in state_city:
        state_city[i["state"]].add(i["city"])
    else:
        cityList.add(i["city"])
        state_city[i["state"]]=cityList

    city_pop[i["city"]]=i["population"]
    city_sent.append("City "+i["city"].title()+" has "+format(int(i["population"]), ',')+" people residing in it.")
    city_sent.append("City "+i["city"].title()+" is in state "+i["state"].title())
    city_sent.append(i["population"]+" people live in the city "+i["city"].title())
    city_sent.append("The population of city "+i["city"].title()+" is "+format(int(i["population"]), ','))
    city_sent.append(format(int(i["population"]), ',')+" number of people live in the city "+i["city"].title())

state_maxpop={}
for s,c in state_city.items():
    city_sent.append("The cities in the state "+s.title()+" are "+" , ".join(state_city[s]).title())
    temp={}
    for c1 in c:
        temp[c1]=city_pop[c1]
    city_max=max(temp.items(), key=operator.itemgetter(1))[0]
    city_min=min(temp.items(), key=operator.itemgetter(1))[0]

    # state_maxpop[s]=st_max
    city_sent.append("The most populous city in "+s.title()+" is "+city_max.title())
    city_sent.append("The least populous city in "+s.title()+" is "+city_min.title())
    city_sent.append(city_max.title()+" is the city with highest population in the state "+s.title())
    city_sent.append(city_min.title()+" is the city with least population in the state "+s.title())

# print(state_maxpop)
max_pop_city=max(city_pop.items(), key=operator.itemgetter(1))[0]
min_pop_city=min(city_pop.items(), key=operator.itemgetter(1))[0]

city_sent.append(max_pop_city.title()+" is the most populous city in USA")
city_sent.append(max_pop_city.title()+" has the largest population in USA")

city_sent.append(min_pop_city.title()+" is the least populous city in USA")
city_sent.append(min_pop_city.title()+" has the lowest population in USA")

# print(max(city_pop.items(), key=operator.itemgetter(1))[0])
# print(city_sent)
db.questions.insert({'cities': city_sent})
