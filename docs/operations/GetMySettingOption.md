# GetMySettingOption

Get a specific setting that is from you.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
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
| key | Avatar's Background (A type of variable called key, this is a value) | ARRAY OF HEX CODE |

## Payload
```json
{
   "operationName": "GetMySettingOption",
   "variables": {},
   "query": "query GetMySettingOption($key: String!) { UserSettings { __typename myAvailableSetting(key: $key) } }"
}
```