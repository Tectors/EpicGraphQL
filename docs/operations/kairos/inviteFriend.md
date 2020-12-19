# inviteFriend

Add/Accept a friend request.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
```graphql
mutation inviteFriend($friendId: String!) {
  Friends {
    invite(friendToInvite: $friendId) {
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
   "operationName": "inviteFriend",
   "variables": {},
   "query": "mutation inviteFriend($friendId: String!) { Friends { __typename invite(friendToInvite: $friendId) { __typename success } } }"
}
```