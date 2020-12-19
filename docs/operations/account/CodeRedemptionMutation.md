# CodeRedemptionMutation

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation CodeRedemptionMutation($country: String!, $identityId: String!, $language: String!, $salesEventId: String!, $codeId: String!, $locale: String!, $codeUseId: String!, $source: String!) {
    CodeRedemption {
        claimFreeCoupon(country: $country, identityId: $identityId, language: $language, salesEventId: $salesEventId) {
            allowRepeatedUsesBySameUser
            batchId
            batchLimit
            batchNumber
            consumptionMetadata {
                amountDisplay {
                    amount
                    currency
                    placement
                    symbol
                }
                applyMerchantGroup
                epicSalesEventId
                minSalesPriceDisplay {
                    amount
                    currency
                    placement
                    symbol
                }
            }
            creator
            code
            codeRuleId
            codeStatus
            codeType
            completedCount
            dateCreated
            distributionDate
            endDate
            freeCouponsRemaining
            maxNumberOfUses
            namespace
            salesEvent {
                currencyRewards {
                    currency {
                        code
                        decimals
                        description
                        priceRanges
                        symbol
                        type
                    }
                    reward
                    minSalePrice
                }
                endDate
                eventName
                freeCouponsRemaining(identityId: $identityId)
                freeVoucherAccountAmount
                grantInitialVoucher
                id
                eventSlug
                eventType
                merchantGroups
                startDate
                voucherEffectiveDays
                voucherExpirationDate
                voucherImages {
                    type
                    url
                }
                voucherMaxAccountAmount
                voucherName
            }
            startDate
            useCount
        }
        lockCode(codeId: $codeId, locale: $locale) {
            success
            data {
                offerId
                namespace
                title
                description
                image
                eulaIds
                entitlementName
                codeUseId
            }
        }
        unlockCode(codeId: $codeId, codeUseId: $codeUseId) {
            success
            data {
                offerId
                namespace
                title
                description
                image
                eulaIds
                entitlementName
                codeUseId
            }
        }
        redeemCode(codeId: $codeId, source: $source, codeUseId: $codeUseId) {
            success
            data {
                offerId
                namespace
                title
                description
                image
                eulaIds
                entitlementName
                codeUseId
            }
        }
    }
}
```

## Variables
```json
{
    "country": "",
    "identityId": "",
    "language": "",
    "salesEventId": "",
    "codeId": "",
    "locale": "",
    "codeUseId": "",
    "source": ""
}
```