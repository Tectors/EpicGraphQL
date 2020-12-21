# FriendsSettings
*Sheesh, this is the 36 operation created.*

Friends notification settings.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation FriendsSettings($value: NotificationSettingsInput!) {
  Friends {
    setNotificationSettings(data: $value) {
     status
     success
      offline {
       suppress_all
      }
    }
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
   "query": "mutation FriendsSettings($value: NotificationSettingsInput!) { Friends { setNotificationSettings(data: $value) { offline { suppress_all } success status } } }"
}
```