# GetFriendSubscriptionsSummary

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> query
```graphql
query GetFriendSubscriptionsSummary {
  PresenceV2 {
    getSubscriptions(namespace: "_") {
      summary {
       account_id
       subscribed_at
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
   "query": "query GetFriendSubscriptionsSummary { PresenceV2 { __typename getSubscriptions(namespace: \"_\") { __typename summary { __typename subscribed_at account_id } } } }"
}
```