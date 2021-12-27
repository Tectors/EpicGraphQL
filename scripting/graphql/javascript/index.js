const GraphQLTag = require('graphql-formatter');
const GraphQLTag2 = require('graphql-tag');
const dedent = require('dedent');
const fs = require('fs');

// <-------------- CONFIG -------------->

const path = '../fi.json';
const entries = require(path).log.entries;

// Trusted GraphQL URLS
const trusted = [
    'https://www.epicgames.com/graphql',
    'https://graphql.unrealengine.com/ue/graphql',
    'https://graphql.epicgames.com/partyhub/graphql',
    'https://graphql.epicgames.com/graphql'
]

// --------------> CONFIG <--------------

const _type = (request, type) => {
    return request.constructor.name === type;
}

/**
 * Censor a object, string, number, boolean, or array to hide important properties that
 * may expose unwanted public information.
 * 
 * [PORTED FROM: scripting/graphql/python/graphql.py] (Tector)
 * @param {String||Number||Boolean||Object||Array} parameter The parameter that'll be censored once passed into this function.
 */
const censor = (parameter, safe=[
    'en-us',
    'us',
    'releasedate',
    'egs',
    'email',
    'en'
]) => {
    // If the parameter is a object
    if (_type(parameter, 'Object')) {
        // For each property in the object
        for (let name in parameter) {
            let value = parameter[name]

            /**
             * If it is allowed to be un-censored.
             * 
             * (HAND-PICKED):
             * - category
             * - sortDir
             * - trendingImage
             * - slug
             * - _metaTags
             * - nextDescription
             * - currencyId
             * - operation
             */
            if (name === 'category' || name === 'sortDir' || name === 'trendingImage' || name === 'slug' || name === '_metaTags' || name === 'nextDescription' || name === 'currencyId' || name === 'operation')
                continue;

            parameter[name] = censor(value);
        }
    }
    // If it's a array
    else if (_type(parameter, 'Array')) {
        // Remove duplicates
        parameter = [...new Map(parameter.map((item, key) => [item[key], item])).values()];

        for (const [index, value] of parameter.entries()) {
            parameter[index] = censor(value);            
        }
    }
    // If it is a different type besides list or object
    else {
        // Highly probable to contain unwanted information
        const probable = [
            'gmail',
            '@'
        ]

        if (_type(parameter, 'String')) {
            // If it is highly probable to contain unwanted information
            // or not safe.
            if (probable.includes(parameter.toLowerCase()) || !safe.includes(parameter.toLowerCase()) || parameter.length == 32) {
                parameter = '';
            }
            // If it is nor, it'll just ignore it and never update it.
        } else {
            parameter =
                // Number
                _type(parameter, 'Number') ? 0 :
                // Boolean
                _type(parameter, 'Boolean') ? false :
                // Default: String
                '';
        }
    }

    return parameter;
}

// For each entry (request) in the log
for (const index in entries) {
    const entry = entries[index];

    const request = entry.request;
    const response = entry.response;
    if (request == null || response == null || request.method == 'OPTIONS')
        continue;
    
    const query = request.queryString;
    const url = request.url;

    if (trusted.filter(domain => url == domain)[0]) {
        const responseText = entry['request']['postData']['text'];
        if (!responseText)
            continue;
    
        const add_comments = (string) => {
            const lines = string.split('\n');
            let reCompiled = '';

            for (const inda in lines)
                reCompiled += `# ${lines[inda]}\n`
            
            return reCompiled
        }

        const responseJSON = JSON.parse(entry['request']['postData']['text']);
        let responseQuery = '';

        const tag = GraphQLTag2(responseJSON.query).definitions[0];
        const name = tag['name'] ? tag['name']['value'] : null || responseJSON.query.split('(')[0].split('\n').pop().trim().replace('query', '').replace('mutation', '').replace(' ');

        const lines = GraphQLTag.format(responseJSON.query).split('\n')
        for (const ind in lines)
            if (lines[ind] != '')
                responseQuery += lines[ind].replace(/	/g, "  ").replace(/^(?:[\t ]*(?:\r?\n|\r))+/gm, '') + '\n';
        
        const variables = responseJSON.variables && Object.keys(responseJSON.variables).length != 0 ? add_comments(JSON.stringify(censor(responseJSON.variables), null, '  ')) : null;
        
        fs.writeFileSync('../../../docs/graphql/sort/' + name + '.graphql', responseQuery.trim().replace('aa37163afe244d3e8a991e0cc71955d6', '') + (variables != null ? '\n\n# Variables:\n' + variables.trim() : ''));
    }

    // Check if it is related to GraphQL at all
    // if (trusted.filter(domain => url.startsWith(domain))[0] && !trusted.filter(domain => url == domain)[0]) {

    //     const find_query = (name) =>
    //         query.filter(property => property.name == name);
        
    //     const name = find_query('operationName')[0].value;
    // }
}