# getFriend

Get friend by friend ID.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query getFriend($friendId: String!) {
  Friends {
    friend(displayNames: true, friendId: $friendId) {
      connections {
       type
       name
      }
      account {
        externalAuths {
         externalDisplayName
         type
        }
      }
     alias
     displayName
     accountId
    }
  }
}
```

## Variables
```json
{
   "friendId": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| friendId | A friend ID. | STRING |

## Payload
```json
{
   "variables": {
      "friendId": ""
   },
   "query": "query getFriend($friendId: String!) { Friends { friend(friendId: $friendId, displayNames: true) { accountId displayName alias account { externalAuths { type externalDisplayName } } connections { name type } } } }"
}
```