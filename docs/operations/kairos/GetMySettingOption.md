# GetMySettingOption

Get a specific setting that is from you.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> query
```graphql
query GetMySettingOption($key: String!) { UserSettings { __typename myAvailableSetting(key: $key) } }
```

## Variables
```json
{
   "key": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| key | None | None |

### Keys
This GraphQL seems to include the key property, here's some ideas of what it could be.

| KEY | DESCRIPTION |
| - | - |
| appInstalled | If the *Fortnite App* is installed. (Kairos) |
| avatarBackground | Avatar's Background (Kairos) |
| avatar | Avatar (Kairos) |

## Payload
```json
{
   "operationName": "GetMySettingOption",
   "variables": {},
   "query": "query GetMySettingOption($key: String!) { UserSettings { __typename myAvailableSetting(key: $key) } }"
}
```