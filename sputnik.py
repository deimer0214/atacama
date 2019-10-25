import json
#https://www.youtube.com/watch?v=9N6a-VLBa2I&t=134s
#https://www.youtube.com/watch?v=oQfNYqz8pLs

with open('UCL_20191022.json') as access_json:
    read_content = json.load(access_json)

def tweets_para_lucho():
    question_access = read_content['Name']
    for question_data in question_access:
        replies_access = question_data['text']
        guarda_tweets.append(replies_access)

guarda_tweets=[]
tweets_para_lucho()

with open('tweets_para_lucho_new', 'w') as file:
    json.dump(guarda_tweets, file)
