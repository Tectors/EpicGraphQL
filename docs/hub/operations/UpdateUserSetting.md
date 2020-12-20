# UpdateUserSetting

Update user settings. (ect. kairos)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
```graphql
mutation UpdateUserSetting($value: String!, $key: String!) {
  UserSettings {
    updateSetting(value: $value, key: $key) {
     success
     __typename
    }
   __typename
  }
}
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
   "variables": {
      "key": "",
      "value": ""
   },
   "query": "mutation UpdateUserSetting($key: String!, $value: String!) { UserSettings { __typename updateSetting(key: $key, value: $value) { __typename success } } }"
}
```