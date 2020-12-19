# unblockFriend

Unblock a friend.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
```graphql
mutation unblockFriend($friendId: String!) { Friends { __typename unblock(friendToUnblock: $friendId) { __typename success } } }
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
   "operationName": "unblockFriend",
   "variables": {},
   "query": "mutation unblockFriend($friendId: String!) { Friends { __typename unblock(friendToUnblock: $friendId) { __typename success } } }"
}
```