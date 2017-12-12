import glob
import json
import os
import requests


# conan's internal joke data api relies on a valid joke_id
# this initial id corresponds with a joke from 12/11/17
INITIAL_ID = '102204'


def make_url(id):
    return 'http://teamcoco.com/x9/xhr/jokes/more/{}/next.json'.format(id)


# fetch and store jokes (one per file)
# this takes awhile (~50 mins)
url = make_url(INITIAL_ID)

while True:
    print('parsing {}...'.format(url))
    response = requests.get(url)
    data = json.loads(response.content.decode('utf-8'))

    if not data:
        break

    for d in data:
        print('{}\n'.format(d['title']))
        fname = 'output/jokes/{}.json'.format(d['id'])
        with open(fname, 'w') as f:
            json.dump(d, f, ensure_ascii=False)

    url = make_url(data[-1]['id'])


# combine all joke data into one json file
joke_files = glob.glob('{}/output/jokes/*'.format(os.getcwd()))
jokes = []

for file in joke_files:
    with open(file) as f:
        jokes.append(json.loads(f.read()))

with open('output/jokes-all.json', 'w') as f:
    json.dump(jokes, f, ensure_ascii=False)


# output jokes (no meta data) to text file
with open("output/jokes-all-clean.txt", "w") as f:
    for joke in jokes:
        f.write('{}\n\n'.format(joke['body']))
