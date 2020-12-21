# GetMyAccount
*Sheesh, this is the 23 operation created.*

Get information about your account.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query GetMyAccount {
  Fortnite {
    myProfile {
     id
     __typename
    }
   __typename
  }
  Account {
    myAccount {
      externalAuths {
       type
       externalDisplayName
       __typename
      }
     country
     email
     displayName
     id
     __typename
    }
   __typename
  }
}
```

## Variables
```json
{}
```
No variables found, if you think this is a mistake contact me at Tector#0001.

## Payload
```json
{
   "variables": {},
   "query": "query GetMyAccount { Account { __typename myAccount { __typename id displayName email country externalAuths { __typename externalDisplayName type } } } Fortnite { __typename myProfile { __typename id } } }"
}
```