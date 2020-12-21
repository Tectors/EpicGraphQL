# UnsubscribeFromFriend
*Sheesh, this is the 21 operation created.*

Unsubscribe from a friend. (Removes notifications from that friend)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation UnsubscribeFromFriend($friendID: String!) {
  PresenceV2 {
    unSubscribeUser(publisherId: $friendID, namespace: "_") {
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
   "query": "mutation UnsubscribeFromFriend($friendID: String!) { PresenceV2 { __typename unSubscribeUser(namespace: \"_\", publisherId: $friendID) { __typename success } } }"
}
```