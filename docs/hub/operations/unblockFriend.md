# unblockFriend

Unblock a friend.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation unblockFriend($friendId: String!) {
  Friends {
    unblock(friendToUnblock: $friendId) {
     success
     __typename
    }
   __typename
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
   "query": "mutation unblockFriend($friendId: String!) { Friends { __typename unblock(friendToUnblock: $friendId) { __typename success } } }"
}
```