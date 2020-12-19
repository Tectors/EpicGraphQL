# deleteFriend

Remove/Decline a friend/request.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
```graphql
mutation deleteFriend($friendId: String!) {
  Friends {
    deleteFriend(friendToDelete: $friendId) {
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
   "variables": {},
   "query": "mutation deleteFriend($friendId: String!) { Friends { __typename deleteFriend(friendToDelete: $friendId) { __typename success } } }"
}
```