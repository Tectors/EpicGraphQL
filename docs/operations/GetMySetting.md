# GetMySetting

Description here, manual action needed.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
query GetMySetting($key: String!) { UserSettings { __typename mySetting(key: $key) { __typename accountId value } } }
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
   "operationName": "GetMySetting",
   "variables": {},
   "query": "query GetMySetting($key: String!) { UserSettings { __typename mySetting(key: $key) { __typename accountId value } } }"
}
```