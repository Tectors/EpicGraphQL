# GetStatusPerService

Status about a service, that is/isn't in kairos.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
query GetStatusPerService($fortniteId: String!, $kairosId: String!, $namespace: String!) { LightSwitch { __typename fortniteStatus: serviceStatus(serviceId: $fortniteId) { __typename status banned } kairosStatus: serviceStatus(serviceId: $kairosId) { __typename status } } SocialBan { __typename summary: getMySocialBanSummary { __typename bans { __typename starts_at ends_at acked duration_s } } } ContentControl { __typename namespace(name: $namespace) { __typename result { __typename canUseVoiceChat } } } }
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
   "operationName": "GetStatusPerService",
   "variables": {},
   "query": "query GetStatusPerService($fortniteId: String!, $kairosId: String!, $namespace: String!) { LightSwitch { __typename fortniteStatus: serviceStatus(serviceId: $fortniteId) { __typename status banned } kairosStatus: serviceStatus(serviceId: $kairosId) { __typename status } } SocialBan { __typename summary: getMySocialBanSummary { __typename bans { __typename starts_at ends_at acked duration_s } } } ContentControl { __typename namespace(name: $namespace) { __typename result { __typename canUseVoiceChat } } } }"
}
```