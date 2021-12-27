import json
import os
import urllib.parse
import textwrap

path = './scripting/graphql/aaaaaaaa.json'

# The content of the har file
content = json.load(open(path, 'r', errors="ignore"))
requests = content['log']['entries']

trusted = [
    'https://www.epicgames.com/graphql',
    'https://graphql.unrealengine.com/ue/graphql'
]

def parse_request_graphql(entry):
    # The graphql query formatted
    query = '\n'.join(textwrap.dedent(json.loads(entry['request']['postData']['text'])['query']).split("\n")[1:]) if textwrap.dedent(json.loads(entry['request']['postData']['text'])['query']).split('\n')[0] == '' else textwrap.dedent(json.loads(entry['request']['postData']['text'])['query'])
    
    print(query)
    # The name of the operation
    name = query.split('\n')[0].split(' ')[1].split('(')[0]

    return query.replace('aa37163afe244d3e8a991e0cc71955d6', ''), name

# Censor properties in a object
def censor_properties(objecter):
    # If a property is a object
    if objecter.__class__ is dict:
        # For each property in the object
        for property in objecter.keys():
            # And set it as well as censoring it
            if property != 'category' and property != 'sortDir' and property != 'trendingImage' and property != 'slug' and property != '_metaTags' and property != 'nextDescription' and property != 'currencyId':
                objecter[property] = censor_properties(objecter[property])
    # If the property is a array
    elif objecter.__class__ is list:
        # If it only includes strings or numbers, only provide one of them
        if objecter.__len__() > 1 and (objecter[0].__class__ is str or objecter[0].__class__ is int):
            # Add one property type of it's self
            objecter = ['' if objecter[0].__class__ is str else 0 if objecter[0].__class__ is int else None]
        else:
            objecter = objecter[:10]

            # If it's not, then do a for each in the object
            for index, property in enumerate(objecter):
                # Censor it as well by the index
                objecter[index] = censor_properties(property)
    # If it is a different type besides list or object
    else:
        # Set it as well as censoring it
        hell_na = ['@']

        if isinstance(objecter, str):
            if "gmail" in objecter:
                objecter = ''
            if isinstance(objecter, str) and objecter != 'en-US' and objecter != 'US' and objecter != 'releaseDate' and objecter != 'EGS' and objecter != 'email':
                objecter = ''
        else:
            objecter = objecter if isinstance(objecter, bool) else '' if isinstance(objecter, str) else 0 if isinstance(objecter, int) else None

    # And return it
    return objecter

added = []

for request in requests:
    _request = request['request']
    response = request['response']

    url = _request['url']

    # NOTE: Only for GraphQL requests with graph text
    # if [_url for _url in trusted if url == _url]:
    #     with open('./docs/graphql/catalog/' + parse_request_graphql(request)[1] + '.graphql', 'w') as a:
    #         a.write(parse_request_graphql(request)[0])
    # NOTE: Only for GraphQL that don't contain the graph text in the postData
    if [_url for _url in trusted if url.startswith(_url)] and not [_url for _url in trusted if url == _url]:
        # Find a query from a name
        def find_query(name):
            return [query for query in _request['queryString'] if query['name'] == name]

        def add_comments(string):
            lines = string.split('\n')
            re_compiled = ''

            for line in lines:
                re_compiled += f'# {line}\n'

            return re_compiled

        name = find_query('operationName')[0]['value']

        bIsUnreal = url.startswith(trusted[1]) # See what I did there? No? Whatever.
        is_operation = find_query('operationName') != []
        directory = ('./docs/graphql/unreal-engine/' if bIsUnreal else './docs/graphql/') + 'operation/' + name + '_' + _request['method'].lower() + '.graphql'

        variables = add_comments(json.dumps(censor_properties(json.loads(urllib.parse.unquote(_request['queryString'][1]['value']))), indent=4, separators=(", ", ": "), sort_keys=True))
        extensions = add_comments(json.dumps(censor_properties(json.loads(urllib.parse.unquote(_request['queryString'][-1]['value']))), indent=4, separators=(", ", ": "), sort_keys=True)) if find_query('extensions') != [] else None
        url_without_query = url.split('?')[0]
        url_censored = url.split('?')[0] + '?'

        for query in _request['queryString']:
            _name = query['name']
            value = query['value']

            if _name == 'operationName':
                url_censored += _name + '=' + value + '&'
            else:
                url_censored += _name + '=' + '[{}]' + '&'

        with open(directory, 'w') as a:
            a.write(f"# {_request['method'].upper()}: {url_censored.rsplit('&', 1)[0]}\n# | {name} |\n\n# Variables:\n{variables}\n" + '# Extensions:\n' + extensions if find_query('extensions') != [] else '')