# SetNotificationSettings

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
```graphql
mutation SetNotificationSettings($friendRequestNotificationSettings: NotificationSettingsInput!, $partyNotificationSettings: NotificationSettingsInput!, $namespace: String!) {
  Friends {
    setNotificationSettings(data: $friendRequestNotificationSettings) {
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
  PartySettings {
    setNotificationSettings(value: $partyNotificationSettings, namespace: $namespace) {
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
   "friendRequestNotificationSettings": {},
   "partyNotificationSettings": {},
   "namespace": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| friendRequestNotificationSettings | None | object |
| partyNotificationSettings | None | object |
| namespace | The short/full name of the game. | String |

## Payload
```json
{
   "variables": {
      "namespace": "",
      "partyNotificationSettings": {
         "offline": {
            "suppress_all": "boolean"
         }
      },
      "friendRequestNotificationSettings": {
         "offline": {
            "suppress_all": "boolean"
         }
      }
   },
   "query": "mutation SetNotificationSettings($namespace: String!, $partyNotificationSettings: NotificationSettingsInput!, $friendRequestNotificationSettings: NotificationSettingsInput!) { PartySettings { __typename setNotificationSettings(namespace: $namespace, value: $partyNotificationSettings) { __typename offline { __typename suppress_all } success status } } Friends { __typename setNotificationSettings(data: $friendRequestNotificationSettings) { __typename offline { __typename suppress_all } success status } } }"
}
```