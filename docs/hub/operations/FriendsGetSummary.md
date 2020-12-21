# FriendsGetSummary
*Sheesh, this is the 29 operation created.*

Get a summary of your friends.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query FriendsGetSummary {
  Friends {
    summary(displayNames: true) {
      blocklist {
       displayName
       accountId
      }
      suggested {
       friendsOnPlatforms
       displayName
       accountId
      }
      outgoing {
        connections {
         type
         name
        }
       displayName
       accountId
      }
      incoming {
        connections {
         type
         name
        }
       displayName
       accountId
      }
      friends {
        connections {
         type
         name
        }
       alias
       displayName
       accountId
      }
    }
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
   "query": "query FriendsGetSummary { Friends { summary(displayNames: true) { friends { accountId displayName alias connections { name type } } incoming { accountId displayName connections { name type } } outgoing { accountId displayName connections { name type } } suggested { accountId displayName friendsOnPlatforms } blocklist { accountId displayName } } } }"
}
```