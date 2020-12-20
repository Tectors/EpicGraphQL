# OrderProcessorQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query OrderProcessorQuery($identityId: String!, $startDate: String!, $endDate: String!, $groupBy: String!, $sortDir: String!, $country: String!, $locale: String!, $category: String!, $namespace: String!, $offerId: String!, $start: Int!, $count: Int!) {
    OrderProcessor {
        salesReport(identityId: $identityId, startDate: $startDate, endDate: $endDate, groupBy: $groupBy, sortDir: $sortDir) {
            reportDate
            identityId
            totalSoldNumber
            totalPurchaseNumber
            totalRefundNumber
            totalChargebackNumber
            totalSoldAmount
            totalPurchaseAmount
            totalRefundAmount
            totalChargebackAmount
            salesDetail {
                totalNumberOfPurchase
                totalNumberOfRefund
                totalNumberOfChargeback
                totalNumberOfOfferSold
                totalSoldAmount
                basePayoutCurrencyCode
                offerId
                catalogOffer {
                    title
                    description
                    longDescription
                    keyImages {
                        type
                        url
                        md5
                        width
                        height
                        size
                        uploadedDate
                    }
                    categories {
                        path
                    }
                    namespace
                    status
                    creationDate
                    lastModifiedDate
                    id
                    developer
                    eulaIds
                    customAttributes {
                        key
                        value
                        type
                    }
                    technicalDetails
                    recurrence
                    items {
                        title
                        description
                        longDescription
                        keyImages {
                            type
                            url
                            md5
                            width
                            height
                            size
                            uploadedDate
                        }
                        categories {
                            path
                        }
                        namespace
                        status
                        creationDate
                        lastModifiedDate
                        id
                        developer
                        eulaIds
                        customAttributes {
                            key
                            value
                            type
                        }
                        technicalDetails
                        releaseInfo {
                            appId
                            compatibleApps
                            platform
                            dateAdded
                        }
                        entitlementName
                        entitlementType
                        dlcItemList
                        mainGameItem
                    }
                    currencyCode
                    currentPrice
                    price(country: $country) {
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
                    promotions(category: $category) {
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
                    basePrice
                    basePriceCurrencyCode
                    recurringPrice
                    freeDays
                    seller {
                        id
                        name
                    }
                    viewableDate
                    effectiveDate
                    vatIncluded
                    isFeatured
                    urlSlug
                    ignoreOrder
                    fulfillToGroup
                    linkedOfferId
                    linkedOfferNs
                    linkedOffer
                    url
                    collectionOfferIds
                    collectionOffers
                    productSlug
                    isCountryAgeBlocked
                    catalogNs {
                        parent
                        taxSkuId
                        displayName
                        eulaIds {
                            value
                            hash
                            empty
                        }
                        store
                        merchantGroup
                        namespaceType
                        accessType
                        sellerRevenueShare
                        addVatToPrice
                        convenienceFee
                        ageGating {
                            country
                            age
                        }
                        name
                        defaultPublic
                        region
                        priceTierType
                        status
                        accountAuthorized
                    }
                    tags {
                        aliases
                        created
                        referenceCount
                        namespace
                        name
                        comment
                        id
                        updated
                        operator
                        status
                    }
                }
                namespace
                merchantGroup
                totalPurchaseAmount
                totalRefundAmount
                totalChargebackAmount
                basePayoutPrice
            }
        }
        countrySalesDetails(identityId: $identityId, namespace: $namespace, offerId: $offerId, startDate: $startDate, endDate: $endDate, start: $start, count: $count, sortDir: $sortDir) {
            paging {
                total
                count
                start
            }
            elements {
                catalogOffer {
                    title
                    description
                    longDescription
                    keyImages {
                        type
                        url
                        md5
                        width
                        height
                        size
                        uploadedDate
                    }
                    categories {
                        path
                    }
                    namespace
                    status
                    creationDate
                    lastModifiedDate
                    id
                    developer
                    eulaIds
                    customAttributes {
                        key
                        value
                        type
                    }
                    technicalDetails
                    recurrence
                    items {
                        title
                        description
                        longDescription
                        keyImages {
                            type
                            url
                            md5
                            width
                            height
                            size
                            uploadedDate
                        }
                        categories {
                            path
                        }
                        namespace
                        status
                        creationDate
                        lastModifiedDate
                        id
                        developer
                        eulaIds
                        customAttributes {
                            key
                            value
                            type
                        }
                        technicalDetails
                        releaseInfo {
                            appId
                            compatibleApps
                            platform
                            dateAdded
                        }
                        entitlementName
                        entitlementType
                        dlcItemList
                        mainGameItem
                    }
                    currencyCode
                    currentPrice
                    price(country: $country) {
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
                    promotions(category: $category) {
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
                    basePrice
                    basePriceCurrencyCode
                    recurringPrice
                    freeDays
                    seller {
                        id
                        name
                    }
                    viewableDate
                    effectiveDate
                    vatIncluded
                    isFeatured
                    urlSlug
                    ignoreOrder
                    fulfillToGroup
                    linkedOfferId
                    linkedOfferNs
                    linkedOffer
                    url
                    collectionOfferIds
                    collectionOffers
                    productSlug
                    isCountryAgeBlocked
                    catalogNs {
                        parent
                        taxSkuId
                        displayName
                        eulaIds {
                            value
                            hash
                            empty
                        }
                        store
                        merchantGroup
                        namespaceType
                        accessType
                        sellerRevenueShare
                        addVatToPrice
                        convenienceFee
                        ageGating {
                            country
                            age
                        }
                        name
                        defaultPublic
                        region
                        priceTierType
                        status
                        accountAuthorized
                    }
                    tags {
                        aliases
                        created
                        referenceCount
                        namespace
                        name
                        comment
                        id
                        updated
                        operator
                        status
                    }
                }
                sumOfPurchasePayoutPrice
                sumOfBasePayoutPrice
                groupByCountry
                saleDay
                numberOfOfferSold
                totalNumberOfPurchase
                merchantGroup
                offerId
                sumOfChargebackPayoutPrice
                totalNumberOfChargeback
                namespace
                basePayoutPrice
                totalRefundAmount
                totalNumberOfRefund
                sumOfRefundPayoutPrice
            }
        }
    }
}
```

## Variables
```json
{
    "identityId": "",
    "startDate": "",
    "endDate": "",
    "groupBy": "",
    "sortDir": "",
    "country": "",
    "locale": "",
    "category": "",
    "namespace": "",
    "offerId": "",
    "start": 0,
    "count": 0
}
```