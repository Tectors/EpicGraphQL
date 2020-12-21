# GetSummary
*Sheesh, this is the 3 operation created.*

Summary of all friend requests including outgoing requests, current friends, blocklist.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query GetSummary {
  Friends {
    summary(displayNames: true) {
      blocklist {
       displayName
       accountId
       __typename
      }
      suggested {
       friendsOnPlatforms
        connections {
         type
         name
         __typename
        }
       displayName
       accountId
       __typename
      }
      outgoing {
        connections {
         type
         name
         __typename
        }
       displayName
       accountId
       __typename
      }
      incoming {
        connections {
         type
         name
         __typename
        }
       displayName
       accountId
       __typename
      }
      friends {
        connections {
         type
         name
         __typename
        }
       created
       alias
       displayName
       accountId
       __typename
      }
     __typename
    }
   __typename
  }
}
```

## Variables
```json
{}
```
No variables found, if you think this is a mistake contact me at Tector#0001.

## Payload
```json
{
   "variables": {},
   "query": "query GetSummary { Friends { __typename summary(displayNames: true) { __typename friends { __typename accountId displayName alias created connections { __typename name type } } incoming { __typename accountId displayName connections { __typename name type } } outgoing { __typename accountId displayName connections { __typename name type } } suggested { __typename accountId displayName connections { __typename name type } friendsOnPlatforms } blocklist { __typename accountId displayName } } } }"
}
```