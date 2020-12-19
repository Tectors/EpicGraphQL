# EulaQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query EulaQuery($id: String!, $locale: String!, $accountId: String!) {
    Eula {
        getLatestEula(id: $id, locale: $locale) {
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
        getLatestAndConvert(id: $id, locale: $locale) {
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
        hasAccountAccepted(id: $id, accountId: $accountId, locale: $locale) {
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
    "locale": "",
    "accountId": ""
}
```