# GetSubscriptionSettings

All of the subscribed data. (ect. Friend notifications)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> query
```graphql
query GetSubscriptionSettings {
  PresenceV2 {
    getSubscriptionSettings(namespace: "_") {
      broadcast {
       enabled
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
{}
```
No variables found, if you think this is a mistake contact me at Tector#0001.

## Payload
```json
{
   "variables": {},
   "query": "query GetSubscriptionSettings { PresenceV2 { __typename getSubscriptionSettings(namespace: \"_\") { __typename broadcast { __typename enabled } } } }"
}
```