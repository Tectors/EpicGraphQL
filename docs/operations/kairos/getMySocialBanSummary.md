# getMySocialBanSummary

Ban history.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> query
```graphql
query getMySocialBanSummary { SocialBan { __typename summary: getMySocialBanSummary { __typename warnings { __typename acked } bans { __typename starts_at ends_at acked duration_s } } } }
```

## Variables
```json
{}
```
No variables found, if you think this is a mistake contact me at Tector#0001.

## Payload
```json
{
   "operationName": "getMySocialBanSummary",
   "variables": {},
   "query": "query getMySocialBanSummary { SocialBan { __typename summary: getMySocialBanSummary { __typename warnings { __typename acked } bans { __typename starts_at ends_at acked duration_s } } } }"
}
```