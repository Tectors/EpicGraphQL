# GetMySetting

Get a Kairos setting.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> query
```graphql
query GetMySetting($key: String!) {
  UserSettings {
    mySetting(key: $key) {
     value
     accountId
     __typename
    }
   __typename
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
   "operationName": "GetMySetting",
   "variables": {},
   "query": "query GetMySetting($key: String!) { UserSettings { __typename mySetting(key: $key) { __typename accountId value } } }"
}
```