# PresenceV2Mutation

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation PresenceV2Mutation($namespace: String!, $value: SubscriptionSettingsInput!, $publisherId: String!) {
    PresenceV2 {
        modifySubscriptionSettings(namespace: $namespace, value: $value) {
            success
        }
        triggerBroadcast(namespace: $namespace) {
            success
        }
        subscribeUser(namespace: $namespace, publisherId: $publisherId) {
            success
        }
        unSubscribeUser(namespace: $namespace, publisherId: $publisherId) {
            success
        }
    }
}
```

## Variables
```json
{
    "namespace": "",
    "value": {
        "broadcast": {
            "enabled": true
        }
    },
    "publisherId": ""
}
```