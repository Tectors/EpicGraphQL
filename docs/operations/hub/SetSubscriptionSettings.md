# SetSubscriptionSettings

Subscription settings.

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
> mutation
```graphql
mutation SetSubscriptionSettings($setting: SubscriptionSettingsInput!) {
  PresenceV2 {
    modifySubscriptionSettings(value: $setting, namespace: "_") {
     success
     __typename
    }
   __typename
  }
}
```

## Variables
```json
{
   "setting": {}
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| setting | None | object |

## Payload
```json
{
   "variables": {},
   "query": "mutation SetSubscriptionSettings($setting: SubscriptionSettingsInput!) { PresenceV2 { __typename modifySubscriptionSettings(namespace: \"_\", value: $setting) { __typename success } } }"
}
```