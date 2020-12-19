# PresenceQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query PresenceQuery($namespace: String!, $circle: String!) {
    Presence {
        getLastOnlineSummary(namespace: $namespace, circle: $circle) {
            summary {
                friendId
                namespace
                circle
                last_online
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