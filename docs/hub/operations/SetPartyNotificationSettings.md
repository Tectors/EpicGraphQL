# SetPartyNotificationSettings

Set party notifications.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation SetPartyNotificationSettings($value: NotificationSettingsInput!, $namespace: String!) {
  PartySettings {
    setNotificationSettings(value: $value, namespace: $namespace) {
     status
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
   "value": {},
   "namespace": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| value | A value of the key | object |
| namespace | The short/full name of the game. | String |

## Payload
```json
{
   "variables": {
      "namespace": "",
      "value": {
         "offline": {
            "suppress_all": Boolean
         }
      }
   },
   "query": "mutation SetPartyNotificationSettings($namespace: String!, $value: NotificationSettingsInput!) { PartySettings { __typename setNotificationSettings(namespace: $namespace, value: $value) { __typename offline { __typename suppress_all } success status } } }"
}
```