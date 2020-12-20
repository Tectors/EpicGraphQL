# AccountMutation

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation AccountMutation($twoFactorRequest: TwoFactorRequest!, $type: [String]!) {
    Account {
        updateTwoFactorAuthentication(twoFactorRequest: $twoFactorRequest) {
            success
        }
        removeThirdPartyLink(type: $type) {
            success
        }
    }
}
```

## Variables
```json
{
    "twoFactorRequest": {
        "state": true
    },
    "type": ""
}
```