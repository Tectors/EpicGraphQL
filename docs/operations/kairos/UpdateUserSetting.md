# UpdateUserSetting

Update user settings. (ect. kairos)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation UpdateUserSetting($key: String!, $value: String!) { UserSettings { __typename updateSetting(key: $key, value: $value) { __typename success } } }
```

## Variables
```json
{
   "value": "",
   "key": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| value | A value of the key | STRING |
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
   "operationName": "UpdateUserSetting",
   "variables": {},
   "query": "mutation UpdateUserSetting($key: String!, $value: String!) { UserSettings { __typename updateSetting(key: $key, value: $value) { __typename success } } }"
}
```