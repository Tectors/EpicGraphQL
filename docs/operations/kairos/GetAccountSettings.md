# GetAccountSettings

Get Kairos ect.. settings from any user.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> query
```graphql
query GetAccountSettings($key: String!, $accountIds: [String]!) { UserSettings { __typename setting(key:$key, accountIds:$accountIds) { __typename value accountId } } }
```

## Variables
```json
{
   "accountIds": {},
   "key": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| accountIds | A array of account ids. | object |
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
   "operationName": "GetAccountSettings",
   "variables": {},
   "query": "query GetAccountSettings($key: String!, $accountIds: [String]!) { UserSettings { __typename setting(key:$key, accountIds:$accountIds) { __typename value accountId } } }"
}
```