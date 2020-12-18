# UpdateUserSetting

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
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
| key | Avatar (A type of variable called key, this is a value) | CID |

## Payload
```json
{
   "operationName": "UpdateUserSetting",
   "variables": {},
   "query": "mutation UpdateUserSetting($key: String!, $value: String!) { UserSettings { __typename updateSetting(key: $key, value: $value) { __typename success } } }"
}
```