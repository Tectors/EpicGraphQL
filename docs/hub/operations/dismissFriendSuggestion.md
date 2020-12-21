# dismissFriendSuggestion
*Sheesh, this is the 44 operation created.*

Dismiss a friend suggestion.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation dismissFriendSuggestion($accountId: String!) {
  Friends {
    dismissFriendSuggestion(suggestionToDismiss: $accountId) {
     success
    }
  }
}
```

## Variables
```json
{
   "accountId": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| accountId | An account id. | STRING |

## Payload
```json
{
   "variables": {
      "accountId": ""
   },
   "query": "mutation dismissFriendSuggestion($accountId: String!) { Friends { dismissFriendSuggestion(suggestionToDismiss: $accountId) { success } } }"
}
```