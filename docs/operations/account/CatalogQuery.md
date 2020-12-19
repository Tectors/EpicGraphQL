# CatalogQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query CatalogQuery($namespace: String!, $id: String!, $locale: String!, $params: CatalogOfferParams!, $countryAgeFilter: CountryAgeFilterInput!, $country: String!, $category: String!, $slug: String!, $count: Int!, $start: Int!, $currencyId: String!, $countryCode: String!, $sortBy: String!, $sortDir: String!, $excludeZeroReferenceCount: Boolean!) {
    Catalog {
        catalogItem(namespace: $namespace, id: $id, locale: $locale) {
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
        catalogOffers(namespace: $namespace, locale: $locale, params: $params, countryAgeFilter: $countryAgeFilter) {
            elements {
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
            paging {
                total
                count
                start
            }
        }
        catalogOffer(namespace: $namespace, id: $id, locale: $locale, countryAgeFilter: $countryAgeFilter) {
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
        catalogOfferBySlug(namespace: $namespace, slug: $slug, locale: $locale, countryAgeFilter: $countryAgeFilter) {
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
        offerSubItems(namespace: $namespace, id: $id, locale: $locale) {
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
        supportedCurrencies(count: $count, start: $start) {
            elements {
                type
                code
                symbol
                description
                decimals
                truncLength
                priceRanges
            }
            paging {
                total
                count
                start
            }
        }
        currency(currencyId: $currencyId) {
            type
            code
            symbol
            description
            decimals
            truncLength
            priceRanges
        }
        countryData(countryCode: $countryCode) {
            currencySymbolPlacement
            defaultCurrency
            paymentCurrency
        }
        lastCatalogUpdate
        catalogNs(namespace: $namespace) {
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
        myCountryFilter {
            hasCountryFilter
            ageGroup
            country
        }
        tags(namespace: $namespace, count: $count, start: $start, locale: $locale, sortBy: $sortBy, sortDir: $sortDir, excludeZeroReferenceCount: $excludeZeroReferenceCount) {
            elements {
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
            paging {
                total
                count
                start
            }
        }
        tagById(namespace: $namespace, id: $id) {
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
}
```

## Variables
```json
{
    "namespace": "",
    "id": "",
    "locale": "",
    "params": {
        "keywords": "",
        "category": "",
        "tag": "",
        "status": "",
        "country": "",
        "sortBy": "",
        "sortDir": "",
        "seller": "",
        "sellerId": "",
        "platform": "",
        "priceRange": "",
        "saleType": "",
        "discountPercentage": "",
        "count": 0,
        "start": 0,
        "effectiveDate": ""
    },
    "countryAgeFilter": {
        "shouldCheck": true,
        "filterCountry": "",
        "filterAgeGroup": 0
    },
    "country": "",
    "category": "",
    "slug": "",
    "count": 0,
    "start": 0,
    "currencyId": "",
    "countryCode": "",
    "sortBy": "",
    "sortDir": "",
    "excludeZeroReferenceCount": true
}
```