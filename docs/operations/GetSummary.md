# GetSummary

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
query GetSummary { Friends { __typename summary(displayNames: true) { __typename friends { __typename accountId displayName alias created connections { __typename name type } } incoming { __typename accountId displayName connections { __typename name type } } outgoing { __typename accountId displayName connections { __typename name type } } suggested { __typename accountId displayName connections { __typename name type } friendsOnPlatforms } blocklist { __typename accountId displayName } } } }
```

## Variables
```json
{}
```
No variables found, if you think this is a mistake contact me at Tector#0001.

## Payload
```json
{
   "operationName": "GetSummary",
   "variables": {},
   "query": "query GetSummary { Friends { __typename summary(displayNames: true) { __typename friends { __typename accountId displayName alias created connections { __typename name type } } incoming { __typename accountId displayName connections { __typename name type } } outgoing { __typename accountId displayName connections { __typename name type } } suggested { __typename accountId displayName connections { __typename name type } friendsOnPlatforms } blocklist { __typename accountId displayName } } } }"
}
```