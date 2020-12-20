# GetLastOnlineSummary

Last time a user was online.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query GetLastOnlineSummary($namespace: String!) {
  PresenceV2 {
    getLastOnlineSummary(circle: "friends", namespace: $namespace) {
      summary {
       last_online
       circle
       namespace
       friendId
       __typename
      }
     __typename
    }
   __typename
  }
}
```

## Variables
```json
{
   "namespace": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| namespace | The short/full name of the game. | String |

## Payload
```json
{
   "variables": {
      "namespace": ""
   },
   "query": "query GetLastOnlineSummary($namespace: String!) { PresenceV2 { __typename getLastOnlineSummary(namespace: $namespace, circle: \"friends\") { __typename summary { __typename friendId namespace circle last_online } } } }"
}
```