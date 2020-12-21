# GetServiceStatus
Get an service status.
*This has different multiple ways to send that'll return different data*

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Kairos Status (including service status)

## Query
```graphql
query GetServiceStatus($kairosId: String!, $fortniteId: String!) {
  SocialBan {
    getMySocialBanSummary {
      bans {
       acked
       ends_at
       starts_at
      }
      warnings {
       acked
      }
    }
  }
  LightSwitch {
    serviceStatus(serviceId: $kairosId) {
     status
    }
    serviceStatus(serviceId: $fortniteId) {
     banned
     status
    }
  }
}
```

## Variables
```json
{
   "kairosId": "",
   "fortniteId": ""
}
```

```json
{
   "variables": {
      "fortniteId": "",
      "kairosId": ""
   },
   "query": "query GetServiceStatus($fortniteId: String!, $kairosId: String!) { LightSwitch { fortniteStatus: serviceStatus(serviceId: $fortniteId) { status banned } kairosStatus: serviceStatus(serviceId: $kairosId) { status } } SocialBan { socialBan: getMySocialBanSummary { warnings { acked } bans { starts_at, ends_at, acked } } } }"
}
```

## Service Status (including if banned)

## Query
```graphql
query GetServiceStatus($serviceId: String!) {
  LightSwitch {
    serviceStatus(serviceId: $serviceId) {
     banned
     status
     allowedActions
    }
  }
}
```

## Variables
```json
{
   "serviceId": ""
}
```

```json
{
   "variables": {
      "serviceId": ""
   },
   "query": "query GetServiceStatus($serviceId: String!) { LightSwitch { serviceStatus(serviceId: $serviceId) { allowedActions status banned } } }"
}
```