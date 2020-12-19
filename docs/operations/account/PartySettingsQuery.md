# PartySettingsQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query PartySettingsQuery($namespace: String!) {
    PartySettings {
        notificationSettings(namespace: $namespace) {
            offline {
                suppress_all
                send_invites
                send_pings
            }
            success
            message
            status
            online {
                suppress_all
                send_invites
                send_pings
            }
            suppress_all
        }
    }
}
```

## Variables
```json
{
    "namespace": ""
}
```