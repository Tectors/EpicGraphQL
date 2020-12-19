# deleteFriend

Remove/Decline a friend/request.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
```graphql
mutation deleteFriend($friendId: String!) { Friends { __typename deleteFriend(friendToDelete: $friendId) { __typename success } } }
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
   "operationName": "deleteFriend",
   "variables": {},
   "query": "mutation deleteFriend($friendId: String!) { Friends { __typename deleteFriend(friendToDelete: $friendId) { __typename success } } }"
}
```