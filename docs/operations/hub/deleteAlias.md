# deleteAlias

Remove a nickname.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
```graphql
mutation deleteAlias($friendId: String!) {
  Friends {
    deleteAlias(friendId: $friendId) {
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
   "query": "mutation deleteAlias($friendId: String!) { Friends { __typename deleteAlias(friendId: $friendId) { __typename success } } }"
}
```