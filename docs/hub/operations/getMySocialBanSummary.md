# getMySocialBanSummary

Ban history.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query getMySocialBanSummary {
  SocialBan {
    getMySocialBanSummary {
      bans {
       duration_s
       acked
       ends_at
       starts_at
       __typename
      }
      warnings {
       acked
       __typename
      }
     __typename
    }
   __typename
  }
}
```

## Variables
```json
{}
```
No variables found, if you think this is a mistake contact me at Tector#0001.

## Payload
```json
{
   "variables": {},
   "query": "query getMySocialBanSummary { SocialBan { __typename summary: getMySocialBanSummary { __typename warnings { __typename acked } bans { __typename starts_at ends_at acked duration_s } } } }"
}
```