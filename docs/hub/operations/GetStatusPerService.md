# GetStatusPerService

Status about a service, that is/isn't in kairos.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> query
```graphql
query GetStatusPerService($namespace: String!, $kairosId: String!, $fortniteId: String!) {
  ContentControl {
    namespace(name: $namespace) {
      result {
       canUseVoiceChat
       __typename
      }
     __typename
    }
   __typename
  }
  SocialBan {
    getMySocialBanSummary {
      bans {
       duration_s
       acked
       ends_at
       starts_at
       __typename
      }
     __typename
    }
   __typename
  }
  LightSwitch {
    serviceStatus(serviceId: $kairosId) {
     status
     __typename
    }
    serviceStatus(serviceId: $fortniteId) {
     banned
     status
     __typename
    }
   __typename
  }
}
```

## Variables
```json
{
   "namespace": "",
   "kairosId": "",
   "fortniteId": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| namespace | The short/full name of the game. | String |
| kairosId | An kairos ID. (ex, kairos) | STRING |
| fortniteId | An Fortnite ID. (ex, Fortnite) | STRING |

## Payload
```json
{
   "variables": {
      "fortniteId": "",
      "kairosId": "",
      "namespace": ""
   },
   "query": "query GetStatusPerService($fortniteId: String!, $kairosId: String!, $namespace: String!) { LightSwitch { __typename fortniteStatus: serviceStatus(serviceId: $fortniteId) { __typename status banned } kairosStatus: serviceStatus(serviceId: $kairosId) { __typename status } } SocialBan { __typename summary: getMySocialBanSummary { __typename bans { __typename starts_at ends_at acked duration_s } } } ContentControl { __typename namespace(name: $namespace) { __typename result { __typename canUseVoiceChat } } } }"
}
```