# GetEula

Get an eula by id and locale.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query GetEula($locale: String!, $id: String!) {
  Eula {
    getLatestAndConvert(locale: $locale, id: $id) {
     version
     title
     locale
     key
     body
     accepted
    }
  }
}
```

## Variables
```json
{
   "locale": "",
   "id": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| locale | Short-hand language. | STRING |
| id | An ID of sort. | STRING |

## Payload
```json
{
   "variables": {
      "id": "",
      "locale": ""
   },
   "query": "query GetEula($id: String!, $locale: String!) { Eula { getLatestAndConvert(id: $id, locale: $locale) { accepted body key locale title version } } }"
}
```