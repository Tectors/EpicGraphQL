# GetFriendSubscriptionsSummary

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query GetFriendSubscriptionsSummary { PresenceV2 { __typename getSubscriptions(namespace: "_") { __typename summary { __typename subscribed_at account_id } } } }
```

## Variables
```json
{}
```
No variables found, if you think this is a mistake contact me at Tector#0001.

## Payload
```json
{
   "operationName": "GetFriendSubscriptionsSummary",
   "variables": {},
   "query": "query GetFriendSubscriptionsSummary { PresenceV2 { __typename getSubscriptions(namespace: \"_\") { __typename summary { __typename subscribed_at account_id } } } }"
}
```