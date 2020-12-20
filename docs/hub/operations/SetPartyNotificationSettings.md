# SetPartyNotificationSettings

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
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
      "value": {},
      "namespace": ""
   },
   "query": "mutation SetPartyNotificationSettings($namespace: String!, $value: NotificationSettingsInput!) { PartySettings { __typename setNotificationSettings(namespace: $namespace, value: $value) { __typename offline { __typename suppress_all } success status } } }"
}
```