# PartnerIntegrationQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query PartnerIntegrationQuery($accountId: String!) {
    PartnerIntegration {
        accountUplayCodes(accountId: $accountId) {
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
```

## Variables
```json
{
    "accountId": ""
}
```