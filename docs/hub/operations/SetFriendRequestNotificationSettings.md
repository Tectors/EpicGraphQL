# SetFriendRequestNotificationSettings

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation SetFriendRequestNotificationSettings($value: NotificationSettingsInput!) {
  Friends {
    setNotificationSettings(data: $value) {
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
   "value": {}
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| value | A value of the key | object |

## Payload
```json
{
   "variables": {
      "value": {
         "offline": {
            "suppress_all": Boolean
         }
      }
   },
   "query": "mutation SetFriendRequestNotificationSettings($value: NotificationSettingsInput!) { Friends { __typename setNotificationSettings(data: $value) { __typename offline { __typename suppress_all } success status } } }"
}
```