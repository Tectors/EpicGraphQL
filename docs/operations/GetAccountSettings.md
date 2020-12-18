# GetAccountSettings

Get Kairos ect.. settings from any user.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
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
| key | Avatar's Background (A type of variable called key, this is a value) | ARRAY OF HEX CODE |

## Payload
```json
{
   "operationName": "GetAccountSettings",
   "variables": {},
   "query": "query GetAccountSettings($key: String!, $accountIds: [String]!) { UserSettings { __typename setting(key:$key, accountIds:$accountIds) { __typename value accountId } } }"
}
```