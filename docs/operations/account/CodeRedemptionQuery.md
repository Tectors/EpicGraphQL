# CodeRedemptionQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query CodeRedemptionQuery($ackByUser: Boolean!, $codeId: String!, $codeType: CouponCodeType!, $count: Int!, $currencyCountry: String!, $identityId: String!, $includeSalesEventInfo: Boolean!, $label: [String]!, $minAvailableLevel: CouponAvailabilityLevel!, $merchantGroup: String!, $namespace: String!, $operatorId: String!, $sortBy: String!, $sortDir: String!, $start: Int!, $locale: String!) {
    CodeRedemption {
        coupons(ackByUser: $ackByUser, codeId: $codeId, codeType: $codeType, count: $count, currencyCountry: $currencyCountry, identityId: $identityId, includeSalesEventInfo: $includeSalesEventInfo, label: $label, minAvailableLevel: $minAvailableLevel, merchantGroup: $merchantGroup, namespace: $namespace, operatorId: $operatorId, sortBy: $sortBy, sortDir: $sortDir, start: $start) {
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
        evaluateCode(codeId: $codeId, locale: $locale) {
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
    "ackByUser": true,
    "codeId": "",
    "codeType": "COUPON, REDEMPTION",
    "count": 0,
    "currencyCountry": "",
    "identityId": "",
    "includeSalesEventInfo": true,
    "label": "",
    "minAvailableLevel": "CONSUMED, DISABLED, EXPIRED, NEVER_USED, RELEASABLE, REMAIN_USE_COUNT",
    "merchantGroup": "",
    "namespace": "",
    "operatorId": "",
    "sortBy": "",
    "sortDir": "",
    "start": 0,
    "locale": ""
}
```