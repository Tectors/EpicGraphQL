# GetAccountSettings
*Sheesh, this is the 2 operation created.*

Get Kairos ect.. settings from any user.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query GetAccountSettings($key: String!) {
  UserSettings {
    setting(accountIds: $accountIds, key: $key) {
     accountId
     value
     __typename
    }
   __typename
  }
}
```

## Variables
```json
{
   "accountIds": [],
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
   "variables": {
      "key": "",
      "accountIds": []
   },
   "query": "query GetAccountSettings($key: String!, $accountIds: [String]!) { UserSettings { __typename setting(key:$key, accountIds:$accountIds) { __typename value accountId } } }"
}
```