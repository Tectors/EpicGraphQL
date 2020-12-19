# ProductQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query ProductQuery($organizationId: String!, $productId: String!) {
    Product {
        product(organizationId: $organizationId, productId: $productId) {
            id
            name
            image
            status
            artifacts {
                artifactId
                liveBuilds {
                    manifestLocation {
                        url
                        expires
                        httpMethod
                    }
                    buildVersion
                    created
                    manifestHash
                    artifactId
                    rvn
                    updated
                    labels {
                        labelName
                        platform
                    }
                }
                rollbackBuilds {
                    manifestLocation {
                        url
                        expires
                        httpMethod
                    }
                    buildVersion
                    created
                    manifestHash
                    artifactId
                    rvn
                    updated
                    labels {
                        labelName
                        platform
                    }
                }
            }
        }
    }
}
```

## Variables
```json
{
    "organizationId": "",
    "productId": ""
}
```