# PartySettings

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation PartySettings($value2: NotificationSettingsInput!, $value1: NotificationSettingsInput!) {
  Friends {
    setNotificationSettings(data: $value2) {
     status
     success
      offline {
       suppress_all
      }
    }
  }
  PartySettings {
    setNotificationSettings(value: $value1, namespace: $namespace) {
     success
     suppress_all
    }
  }
}
```

## Variables
```json
{
   "value2": {},
   "value1": {},
   "value": {}
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| value2 | None | object |
| value1 | None | object |
| value | A value of the key | object |

## Payload
```json
{
   "variables": {
      "value": {
         "offline": {
            "suppress_all": Boolean
         }
      },
      "value1": {
         "offline": {
            "suppress_all": Boolean
         }
      },
      "value2": {
         "offline": {
            "suppress_all": Boolean
         }
      }
   },
   "query": "mutation PartySettings ($namespace: String, $value1: NotificationSettingsInput!,$value2: NotificationSettingsInput!) { PartySettings { setNotificationSettings(namespace: $namespace, value: $value1) { suppress_all success } } Friends { setNotificationSettings(data: $value2) { offline { suppress_all } success status } } }"
}
```