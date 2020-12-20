# EulaMutation

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation EulaMutation($id: String!, $accountId: String!, $version: Int!, $locale: String!) {
    Eula {
        acceptEula(id: $id, accountId: $accountId, version: $version, locale: $locale) {
            key
            version
            revision
            title
            body
            locale
            createdTimestamp
            lastModifiedTimestamp
            agentUserName
            status
            custom
            accepted
        }
    }
}
```

## Variables
```json
{
    "id": "",
    "accountId": "",
    "version": 0,
    "locale": ""
}
```