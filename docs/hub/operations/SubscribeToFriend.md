# SubscribeToFriend
*Sheesh, this is the 24 operation created.*

Subscribe to your friend.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation SubscribeToFriend($friendID: String!) {
  PresenceV2 {
    subscribeUser(publisherId: $friendID, namespace: "_") {
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
   "friendID": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| friendID | None | None |

## Payload
```json
{
   "variables": {
      "friendID": ""
   },
   "query": "mutation SubscribeToFriend($friendID: String!) { PresenceV2 { __typename subscribeUser(namespace: \"_\", publisherId: $friendID) { __typename success } } }"
}
```