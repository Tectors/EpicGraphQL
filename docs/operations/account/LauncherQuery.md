# LauncherQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query LauncherQuery($platform: Platform!, $label: Label!, $locale: String!, $namespace: String!, $offerId: String!, $cursor: String!, $params: LauncherLibraryItemParams!, $offerParams: [OfferParams]!) {
    Launcher {
        appBuilds(platform: $platform, label: $label) {
            appName
            labelName
            buildVersion
            catalogItemId
            namespace
            assetId
            catalogItem(locale: $locale) {
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
        }
        entitledOfferItems(namespace: $namespace, offerId: $offerId) {
            namespace
            offerId
            entitledToAllItemsInOffer
            entitledToAnyItemInOffer
            items {
                itemId
                entitledToItem
            }
        }
        libraryItems(cursor: $cursor, params: $params) {
            records {
                namespace
                catalogItemId
                appName
                catalogItem(locale: $locale) {
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
            }
            responseMetadata {
                nextCursor
            }
        }
        prerequisites(offerParams: $offerParams) {
            namespace
            offerId
            nsOfferIds
            missingPrerequisiteItems
            satisfiesPrerequisites
        }
    }
}
```

## Variables
```json
{
    "platform": "Windows, Win32, Mac, iOS, Android, Linux",
    "label": "Live, Production, Development",
    "locale": "",
    "namespace": "",
    "offerId": "",
    "cursor": "",
    "params": {
        "platform": "",
        "limit": 0,
        "excludeNs": [
            ""
        ]
    },
    "offerParams": {
        "namespace": "",
        "offerId": ""
    }
}
```