# accountQuery

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query accountQuery {
  Account {
    account(email: $email, displayName: $displayName, id: $id) {
      externalAuths {
       externalDisplayName
       type
      }
     friendshipStatus
     displayName
     id
    }
  }
}
```

## Variables
```json
{
   "email": "",
   "displayName": "",
   "id": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| email | None | None |
| displayName | None | None |
| id | An ID of sort. | STRING |

## Payload
```json
{
   "variables": {
      "id": "",
      "displayName": "",
      "email": ""
   },
   "query": "query accountQuery($id: String, $displayName: String, $email: String) { Account { account(id: $id, displayName: $displayName, email: $email) { id, displayName, friendshipStatus externalAuths { type externalDisplayName } } } }"
}
```