# MediaQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query MediaQuery($mediaRefId: String!) {
    Media {
        getMediaRef(mediaRefId: $mediaRefId) {
            accountId
            id
            outputs {
                contentType
                duration
                height
                profile
                url
                width
                key
            }
            namespace
            profile
            recipe
        }
    }
}
```

## Variables
```json
{
    "mediaRefId": ""
}
```