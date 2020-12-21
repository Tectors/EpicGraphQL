# EulaAccepted

If a eula was accepted. (Does not work on fortnite tokens, beware)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query EulaAccepted($locale: String!, $accountId: String!, $id: String!) {
  Eula {
    hasAccountAccepted(locale: $locale, accountId: $accountId, id: $id) {
     accepted
    }
  }
}
```

## Variables
```json
{
   "accountId": "",
   "locale": "",
   "id": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| accountId | An account id. | STRING |
| locale | Short-hand language. | STRING |
| id | An ID of sort. | STRING |

## Payload
```json
{
   "variables": {
      "id": "",
      "locale": "",
      "accountId": ""
   },
   "query": "query EulaAccepted($id: String!, $accountId:String!, $locale:String!) { Eula { hasAccountAccepted(id: $id, accountId: $accountId, locale: $locale) { accepted } } }"
}
```