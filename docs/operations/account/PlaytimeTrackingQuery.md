# PlaytimeTrackingQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query PlaytimeTrackingQuery($accountId: String!, $artifactId: String!) {
    PlaytimeTracking {
        artifact(accountId: $accountId, artifactId: $artifactId) {
            accountId
            artifactId
            totalTime
        }
        total(accountId: $accountId) {
            accountId
            artifactId
            totalTime
        }
    }
}
```

## Variables
```json
{
    "accountId": "",
    "artifactId": ""
}
```