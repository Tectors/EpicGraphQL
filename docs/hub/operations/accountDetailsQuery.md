# accountDetailsQuery

Details about accounts using only account ids.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query accountDetailsQuery {
  Account {
    accounts(accountIds: $accountIds) {
      externalAuths {
       externalDisplayName
       type
      }
     displayName
     id
    }
  }
}
```

## Variables
```json
{
   "accountIds": []
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| accountIds | A array of account ids. | object |

## Payload
```json
{
   "variables": {
      "accountIds": []
   },
   "query": "query accountDetailsQuery($accountIds: [String]!) { Account { accounts(accountIds: $accountIds) { id displayName externalAuths { type externalDisplayName } } } }"
}
```