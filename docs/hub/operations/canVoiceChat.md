# canVoiceChat
*Sheesh, this is the 32 operation created.*

Able to use voice chat in namespace.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query canVoiceChat($namespace: String!) {
  ContentControl {
    namespace(name: $namespace) {
      result {
       canUseVoiceChat
      }
    }
  }
}
```

## Variables
```json
{
   "namespace": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| namespace | The short/full name of the game. | String |

## Payload
```json
{
   "variables": {
      "namespace": ""
   },
   "query": "query canVoiceChat($namespace: String!) { ContentControl{ namespace(name: $namespace) { result { canUseVoiceChat } } } }"
}
```