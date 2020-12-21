# unSubscribeUser

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation unSubscribeUser($publisherId: String!) {
  PresenceV2 {
    unSubscribeUser(publisherId: $publisherId, namespace: "_") {
     success
    }
  }
}
```

## Variables
```json
{
   "publisherId": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| publisherId | None | None |

## Payload
```json
{
   "variables": {
      "publisherId": ""
   },
   "query": "mutation unSubscribeUser($publisherId: String!){ PresenceV2 { unSubscribeUser(namespace: \"_\", publisherId: $publisherId) { success } } }"
}
```