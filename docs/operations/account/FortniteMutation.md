# FortniteMutation

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation FortniteMutation($report: ReportPlayer!) {
    Fortnite {
        reportPlayer(report: $report) {
            success
            status
            errorCode
            errorMessage
        }
    }
}
```

## Variables
```json
{
    "report": {
        "reporterAccountId": "",
        "offenderAccountId": "",
        "reason": "",
        "subGameName": "",
        "details": "",
        "gameSessionId": "",
        "playlistName": "",
        "reporterPlatform": "",
        "offenderPlatform": "",
        "partyId": "",
        "isPartyReport": true,
        "markedAsKnown": true,
        "blockedUserRequested": true
    }
}
```