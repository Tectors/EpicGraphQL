# subscribeUser

Subscribe to an user.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation subscribeUser($publisherId: String!) {
  PresenceV2 {
    subscribeUser(publisherId: $publisherId, namespace: "_") {
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
   "query": "mutation subscribeUser($publisherId: String!){ PresenceV2 { subscribeUser(namespace: \"_\", publisherId: $publisherId) { success } } }"
}
```