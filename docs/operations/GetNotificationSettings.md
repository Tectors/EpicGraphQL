# GetNotificationSettings

Notification settings.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
query GetNotificationSettings($namespace: String!) { Friends { __typename notificationSettings { __typename offline { __typename suppress_all } success message } } PartySettings { __typename notificationSettings(namespace: $namespace) { __typename offline { __typename suppress_all } success message } } }
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
   "operationName": "GetNotificationSettings",
   "variables": {},
   "query": "query GetNotificationSettings($namespace: String!) { Friends { __typename notificationSettings { __typename offline { __typename suppress_all } success message } } PartySettings { __typename notificationSettings(namespace: $namespace) { __typename offline { __typename suppress_all } success message } } }"
}
```