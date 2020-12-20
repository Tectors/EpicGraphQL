# TransientStreamQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query TransientStreamQuery($countryCode: String!, $locale: String!) {
    TransientStream {
        myTransientFeed(countryCode: $countryCode, locale: $locale) {
            id
            activity {
                ns
                created_at
                type
            }
        }
    }
}
```

## Variables
```json
{
    "countryCode": "",
    "locale": ""
}
```