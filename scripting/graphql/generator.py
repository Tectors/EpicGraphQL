import json
import os
import textwrap

# The path to the HAR file exported from the Chrome Browser
path = './scripting/graphql/aaaaaaaa.json'

# The content of the har file
content = json.load(open(path, 'r', errors="ignore"))

# We need to check if the url starts with something api related
# Since that is the point
related = [
    'https://www.epicgames.com/fortnite/en-US/api/',
    'https://www.epicgames.com/fortnite/ajax/',
    'https://www.unrealengine.com/api/v2/',
    'https://www.epicgames.com/account/v2/',
    'https://payment-website-pci.ol.epicgames.com/',
    'https://store-content-ipv4.ak.epicgames.com/api/en-US/',
    'https://www.epicgames.com/help/api/'
]

# So let's get the requests from the HAR file

# For each logged request
for entry in content['log']['entries']:
    # Set some variables from the log
    request = entry['request']
    url = request['url']
    response = entry['response']

    # Let's parse the headers in a format
    headers = ''

    # Also parse the queries into no data provided
    query = ''

    # Query Data
    query_understanding = ''

    json_content = {}

    # For each query param in the request
    for param in request['queryString']:
        query += '&{0}={1}'.format(param['name'], param['value'])

    form_data = ''

    # For each query param in the request
    if "postData" in request.keys() and request['postData']['mimeType'] == 'application/x-www-form-urlencoded':
        for param in request['postData']['params']:
            form_data += '&{0}={1}'.format(param['name'], param['value'])

    # For each header in the request
    for header in request['headers']:
        # Set the normal vars
        name = header['name']
        value = header['value']

        # A filter
        header_name_filters = ['Cookies', 'x-xsrf-token', 'cookie', ':', 'X-requested-with']

        if name.startswith(':') or name.lower().startswith('sec-') or name.lower() == 'host':
            continue

        # Add it to the headers string
        headers += '{0}: {1}\n'.format(name.capitalize(), value if not [filtered for filtered in header_name_filters if name.startswith(filtered)] else 'Removed')

    # If it is related
    if [related for related in related if url.startswith(related)]:
        if "content" in response.keys() and "text" in response['content'].keys():
            if response['content']['text'] != '':
                if "{" in response['content']['text']:
                    uncensored = json.loads(response['content']['text'])
                    censored = [] if isinstance(uncensored, list) else {}

                    # Censor properties in a object
                    def censor_properties(objecter):
                        # If a property is a object
                        if objecter.__class__ is dict:
                            # For each property in the object
                            for property in objecter.keys():
                                # And set it as well as censoring it
                                objecter[property] = censor_properties(objecter[property])
                        # If the property is a array
                        elif objecter.__class__ is list:
                            objecter = objecter[:8]

                            # If it only includes strings or numbers, only provide one of them
                            if objecter.__len__() > 1 and (objecter[0].__class__ is str or objecter[0].__class__ is int):
                                # Add one property type of it's self
                                objecter = ['' if objecter[0].__class__ is str else 0 if objecter[0].__class__ is int else None]
                            else:


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
                                if isinstance(objecter, str):
                                    objecter = ''
                            else:
                                objecter = objecter if isinstance(objecter, bool) else '' if isinstance(objecter, str) else 0 if isinstance(objecter, int) else None

                        # And return it
                        return objecter

                    path = './docs/endpoints/' + url.split('/', 3)[3].replace('en-US/', '').rsplit('/', 1)[0].split('?')[0] + '/'

                    if not os.path.exists(path):
                        os.makedirs(path)
                    
                    request_data = '' if not "postData" in request.keys() else '\n\n' + form_data.split('&', 1)[-1] if request['postData']['mimeType'] == 'application/x-www-form-urlencoded' else '\n\n' + json.dumps(censor_properties(request['postData']['text']), sort_keys=True, indent=4) if "postData" in request.keys() and "text" in request['postData'].keys() else 'a'
                    response_data = '\n' + json.dumps(censor_properties(uncensored), sort_keys=True, indent=4)

                    with open(path + url.split('/', 3)[3].replace('en-US/', '').rsplit('/', 1)[1].split('?')[0] + '.{0}'.format(request['method'].lower()), 'w') as r:
                        r.write('{3} {0} {1}\nHost: {4}\n{2}{5}\n\nResponse: {6}\n{7}'.format(url.split('?')[0] + query.replace('&', '?', 1), response['httpVersion'].upper(), '\n'.join(list(set(headers.split('\n')))), request['method'], url.split("//")[-1].split("/")[0].split('?')[0], request_data, str(response['status']) + ' ' + response['httpVersion'].upper(), response_data))