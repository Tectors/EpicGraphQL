# blockFriend

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
mutation blockFriend($friendId: String!) { Friends { __typename block(friendToBlock: $friendId) { __typename success } } }
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
   "operationName": "blockFriend",
   "variables": {},
   "query": "mutation blockFriend($friendId: String!) { Friends { __typename block(friendToBlock: $friendId) { __typename success } } }"
}
```