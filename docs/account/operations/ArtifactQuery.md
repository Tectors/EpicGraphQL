# ArtifactQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query ArtifactQuery($organizationId: String!, $productId: String!, $id: String!, $labelFilter: String!) {
    Artifact {
        artifact(organizationId: $organizationId, productId: $productId, id: $id, labelFilter: $labelFilter) {
            items {
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
            cursors {
                before
                after
            }
        }
    }
}
```

## Variables
```json
{
    "organizationId": "",
    "productId": "",
    "id": "",
    "labelFilter": ""
}
```