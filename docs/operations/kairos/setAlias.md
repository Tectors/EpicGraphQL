# setAlias

Set nickname to user.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation setAlias($friendId: String!, $alias: String!) { Friends { __typename setAlias(friendId: $friendId, alias: $alias) { __typename success } } }
```

## Variables
```json
{
   "alias": "",
   "friendId": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| alias | An nickname. | STRING |
| friendId | A friend ID. | STRING |

## Payload
```json
{
   "operationName": "setAlias",
   "variables": {},
   "query": "mutation setAlias($friendId: String!, $alias: String!) { Friends { __typename setAlias(friendId: $friendId, alias: $alias) { __typename success } } }"
}
```