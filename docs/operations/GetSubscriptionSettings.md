# GetSubscriptionSettings

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
query GetSubscriptionSettings { PresenceV2 { __typename getSubscriptionSettings(namespace: "_") { __typename broadcast { __typename enabled } } } }
```

## Variables
```json
{}
```
No variables found, if you think this is a mistake contact me at Tector#0001.

## Payload
```json
{
   "operationName": "GetSubscriptionSettings",
   "variables": {},
   "query": "query GetSubscriptionSettings { PresenceV2 { __typename getSubscriptionSettings(namespace: \"_\") { __typename broadcast { __typename enabled } } } }"
}
```