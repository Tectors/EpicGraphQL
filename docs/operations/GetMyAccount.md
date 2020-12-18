# GetMyAccount

Get information about your account.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```
query GetMyAccount { Account { __typename myAccount { __typename id displayName email country externalAuths { __typename externalDisplayName type } } } Fortnite { __typename myProfile { __typename id } } }
```

## Variables
```json
{}
```
No variables found, if you think this is a mistake contact me at Tector#0001.

## Payload
```json
{
   "operationName": "GetMyAccount",
   "variables": {},
   "query": "query GetMyAccount { Account { __typename myAccount { __typename id displayName email country externalAuths { __typename externalDisplayName type } } } Fortnite { __typename myProfile { __typename id } } }"
}
```