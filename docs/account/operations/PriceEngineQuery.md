# PriceEngineQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query PriceEngineQuery($country: String!, $identityId: String!, $namespace: String!, $calculateTax: Boolean!, $lineOffers: [LineOfferReq]!, $locale: String!, $salesEventId: String!, $currency: String!, $eventDate: String!, $eventName: String!, $merchantGroup: String!, $offerId: String!) {
    PriceEngine {
        price(country: $country, identityId: $identityId, namespace: $namespace, calculateTax: $calculateTax, lineOffers: $lineOffers) {
            zipcode
            totalTax {
                taxable
                taxDetails {
                    jurisName
                    country
                    taxable
                    jurisType
                    rate
                    tax
                    region
                    taxName
                }
                rate
                discount
                tax
                taxCode
                taxCalculated
            }
            country
            totalPrice {
                unitPrice
                originalUnitPrice
                discountPercentage {
                    intVal {
                        signum
                        mag
                        bit
                        probablePrime
                    }
                    scale
                }
                convenienceFee
                basePayoutCurrencyCode
                originalPrice
                discountPrice
                vat
                discount
                voucherDiscount
                basePayoutPrice
                currencyCode
                fmtPrice(locale: $locale) {
                    originalPrice
                    discountPrice
                    intermediatePrice
                }
                currencyInfo {
                    type
                    code
                    symbol
                    description
                    decimals
                    truncLength
                    priceRanges
                }
            }
            coupons
            identityId
            namespace
            invoiceId
            totalPaymentPrice {
                paymentCurrencyCode
                paymentCurrencyAmount
                paymentCurrencySymbol
                paymentCurrencyExchangeRate
            }
            lineOffers {
                ref
                quantity
                taxSkuId
                price {
                    unitPrice
                    originalUnitPrice
                    discountPercentage {
                        intVal {
                            signum
                            mag
                            bit
                            probablePrime
                        }
                        scale
                    }
                    convenienceFee
                    basePayoutCurrencyCode
                    originalPrice
                    discountPrice
                    vat
                    discount
                    basePayoutPrice
                    currencyCode
                }
                appliedRules {
                    discountSetting {
                        discountType
                        discountValue
                        discountPercentage
                    }
                    endDate
                    saleType
                    name
                    namespace
                    regionIds
                    id
                    promotionSetting {
                        promotionType
                        discountOffers {
                            offerId
                        }
                    }
                    conditions {
                        conditionValue
                        condiftionType
                    }
                    startDate
                    initiatedBy
                    promotionStatus
                }
                lineId
                offerId
                tax {
                    taxable
                    taxDetails {
                        jurisName
                        country
                        taxable
                        jurisType
                        rate
                        tax
                        region
                        taxName
                    }
                    rate
                    discount
                    tax
                    taxCode
                    taxCalculated
                }
            }
            taxCalculationStatus
        }
        promotions(namespace: $namespace) {
            promotionalOffers {
                key
                promotionalOffers {
                    id
                    name
                    namespace
                    startDate
                    endDate
                    saleType
                    promotionalStatus
                    conditions {
                        conditionType
                        conditionValue
                    }
                    discountSetting {
                        discountType
                        discountValue
                        discountPercentage
                    }
                    promotionSetting {
                        promotionType
                        discountOffers {
                            offerId
                        }
                    }
                    initiatedBy
                }
            }
            upcomingPromotionalOffers {
                key
                promotionalOffers {
                    id
                    name
                    namespace
                    startDate
                    endDate
                    saleType
                    promotionalStatus
                    conditions {
                        conditionType
                        conditionValue
                    }
                    discountSetting {
                        discountType
                        discountValue
                        discountPercentage
                    }
                    promotionSetting {
                        promotionType
                        discountOffers {
                            offerId
                        }
                    }
                    initiatedBy
                }
            }
        }
        salesEvent(salesEventId: $salesEventId) {
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
        salesEvents(currency: $currency, eventDate: $eventDate, eventName: $eventName, merchantGroup: $merchantGroup, offerId: $offerId) {
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
    }
}
```

## Variables
```json
{
    "country": "",
    "identityId": "",
    "namespace": "",
    "calculateTax": true,
    "lineOffers": {
        "unitPrice": 0,
        "quantity": 0,
        "offerId": "",
        "category": ""
    },
    "locale": "",
    "salesEventId": "",
    "currency": "",
    "eventDate": "",
    "eventName": "",
    "merchantGroup": "",
    "offerId": ""
}
```