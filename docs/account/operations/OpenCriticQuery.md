# OpenCriticQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query OpenCriticQuery($sku: String!) {
    OpenCritic {
        productReviews(sku: $sku) {
            award
            id
            name
            openCriticScore
            openCriticUrl
            percentRecommended
            reviewCount
            topReviews {
                author
                displayScore
                externalUrl
                language
                OutletId
                outletName
                publishedDate
                score
                ScoreFormat {
                    description
                    id
                }
                snippet
            }
        }
    }
}
```

## Variables
```json
{
    "sku": ""
}
```