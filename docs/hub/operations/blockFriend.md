# blockFriend

Block a friend.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
```graphql
mutation blockFriend($friendId: String!) {
  Friends {
    block(friendToBlock: $friendId) {
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
   "query": "mutation blockFriend($friendId: String!) { Friends { __typename block(friendToBlock: $friendId) { __typename success } } }"
}
```