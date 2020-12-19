# SocialBanQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query SocialBanQuery {
    SocialBan {
        getMySocialBan {
            starts_at
            ends_at
            acked
            duration_s
        }
        getMySocialBanSummary {
            warnings {
                acked
            }
            bans {
                starts_at
                ends_at
                acked
                duration_s
            }
        }
    }
}
```

## Variables
```json
{}
```