# UserSettingsQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query UserSettingsQuery($key: String!, $accountIds: [String]!) {
    UserSettings {
        mySetting(key: $key) {
            accountId
            value
        }
        myAvailableSetting(key: $key)
        setting(key: $key, accountIds: $accountIds) {
            accountId
            value
        }
    }
}
```

## Variables
```json
{
    "key": "",
    "accountIds": ""
}
```