# PresenceV2Query

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query PresenceV2Query($namespace: String!, $circle: String!) {
    PresenceV2 {
        getLastOnlineSummary(namespace: $namespace, circle: $circle) {
            summary {
                friendId
                namespace
                circle
                last_online
            }
        }
        getSubscriptionSettings(namespace: $namespace) {
            broadcast {
                enabled
            }
        }
        getSubscriptions(namespace: $namespace) {
            summary {
                subscribed_at
                account_id
            }
        }
    }
}
```

## Variables
```json
{
    "namespace": "",
    "circle": ""
}
```