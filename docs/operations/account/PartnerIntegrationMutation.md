# PartnerIntegrationMutation

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation PartnerIntegrationMutation($accountId: String!, $uplayAccountId: String!, $gameId: String!, $platformToken: String!) {
    PartnerIntegration {
        claimUplayCode(accountId: $accountId, uplayAccountId: $uplayAccountId, gameId: $gameId) {
            success
            data {
                epicEntitlement {
                    entitlementId
                    catalogItemId
                    entitlementName
                    country
                }
                gameId
                epicAccountId
                uplayAccountId
                redeemedOnUplay
                redemptionTimestamp
                assignmentTimestam
                regionCode
            }
        }
        redeemAllPendingCodes(accountId: $accountId, uplayAccountId: $uplayAccountId, platformToken: $platformToken) {
            success
            data {
                epicEntitlement {
                    entitlementId
                    catalogItemId
                    entitlementName
                    country
                }
                gameId
                epicAccountId
                uplayAccountId
                redeemedOnUplay
                redemptionTimestamp
                assignmentTimestam
                regionCode
            }
        }
    }
}
```

## Variables
```json
{
    "accountId": "",
    "uplayAccountId": "",
    "gameId": "",
    "platformToken": ""
}
```