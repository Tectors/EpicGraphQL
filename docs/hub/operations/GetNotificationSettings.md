# GetNotificationSettings

Notification settings.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query GetNotificationSettings($namespace: String!) {
  PartySettings {
    notificationSettings(namespace: $namespace) {
     message
     success
      offline {
       suppress_all
       __typename
      }
     __typename
    }
   __typename
  }
  Friends {
    notificationSettings {
     message
     success
      offline {
       suppress_all
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
   "query": "query GetNotificationSettings($namespace: String!) { Friends { __typename notificationSettings { __typename offline { __typename suppress_all } success message } } PartySettings { __typename notificationSettings(namespace: $namespace) { __typename offline { __typename suppress_all } success message } } }"
}
```