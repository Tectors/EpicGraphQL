# GetUserSettings
*Sheesh, this is the 35 operation created.*

User settings from you.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query GetUserSettings($key: String!) {
  UserSettings {
    mySetting(key: $key) {
     value
     accountId
    }
  }
}
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
   "variables": {
      "key": ""
   },
   "query": "query GetUserSettings($key: String!) { UserSettings { mySetting(key: $key) { accountId value } } }"
}
```