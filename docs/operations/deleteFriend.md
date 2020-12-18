# deleteFriend

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
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