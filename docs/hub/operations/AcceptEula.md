# AcceptEula

Accept an eula.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation AcceptEula($accountId: String!, $version: Int!, $locale: String!, $id: String!) {
  Eula {
    acceptEula(accountId: $accountId, version: $version, locale: $locale, id: $id) {
     accepted
    }
  }
}
```

## Variables
```json
{
   "version": 0,
   "accountId": "",
   "locale": "",
   "id": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| version | None | number |
| accountId | An account id. | STRING |
| locale | Short-hand language. | STRING |
| id | An ID of sort. | STRING |

## Payload
```json
{
   "variables": {
      "id": "",
      "locale": "",
      "accountId": "",
      "version": 0
   },
   "query": "mutation AcceptEula($id: String!, $locale: String!, $version: Int!, $accountId: String!) { Eula { acceptEula(id: $id, locale: $locale, version: $version, accountId: $accountId) { accepted } } }"
}
```