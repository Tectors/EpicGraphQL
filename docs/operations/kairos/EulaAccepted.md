# EulaAccepted

If the Eula was accepted.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> query
```graphql
query EulaAccepted($locale: String!, $accountId: String!, $id: String!) {
  Eula {
    hasAccountAccepted(locale: $locale, accountId: $accountId, id: $id) {
     accepted
     __typename
    }
   __typename
  }
}
```

## Variables
```json
{
   "locale": "",
   "accountId": "",
   "id": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| locale | Short-hand language. | STRING |
| accountId | An account id. | STRING |
| id | An ID of sort. | STRING |

## Payload
```json
{
   "variables": {},
   "query": "query EulaAccepted($id:String!, $accountId:String!, $locale:String!) { Eula { __typename hasAccountAccepted(id: $id, accountId: $accountId, locale: $locale) { __typename accepted } } }"
}
```