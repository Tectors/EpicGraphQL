# FortniteQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query FortniteQuery {
    Fortnite {
        myProfile {
            id
            character {
                templateId
                quantity
                attributes {
                    item_seen
                    favorite
                    level
                    variants {
                        active
                        channel
                        owned
                    }
                }
            }
            backpack {
                templateId
            }
        }
        getCurrentStoreOffers {
            refreshIntervalHrs
            dailyPurchaseHrs
            expiration
            storefronts {
                name
                catalogEntries {
                    devName
                    offerId
                    dailyLimit
                    weeklyLimit
                    monthlyLimit
                    categories
                    prices {
                        currencyType
                        currencySubtype
                        regularPrice
                        finalPrice
                        saleExpiration
                        basePrice
                    }
                    displayAssetPath
                    itemGrants {
                        templateId
                        quantity
                    }
                    sortPriority
                    catalogGroupPriority
                    assetName
                }
            }
            success
        }
    }
}
```

## Variables
```json
{}
```