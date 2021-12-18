import json
import os
import textwrap

path = './scripting/graphql/tests.json'

# The content of the har file
content = json.load(open(path, 'r', errors="ignore"))

def parse_request_graphql(entry):
    # The graphql query formatted
    query = '\n'.join(textwrap.dedent(json.loads(entry['request']['postData']['text'])['query']).split("\n")[1:]) if textwrap.dedent(json.loads(entry['request']['postData']['text'])['query']).split('\n')[0] == '' else textwrap.dedent(json.loads(entry['request']['postData']['text'])['query'])

    # The name of the operation
    name = query.split('\n')[0].split(' ')[1].split('(')[0]

    return query, name

for entry in content['log']['entries']:
    if entry['request']['url'] == 'https://www.epicgames.com/graphql' or entry['request']['url'] == 'https://graphql.unrealengine.com/ue/graphql':
        with open('./docs/graphql/catalog/' + parse_request_graphql(entry)[1] + '.graphql', 'w') as a:
            a.write(parse_request_graphql(entry)[0])