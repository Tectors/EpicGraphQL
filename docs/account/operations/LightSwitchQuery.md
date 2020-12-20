# LightSwitchQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query LightSwitchQuery($serviceId: String!) {
    LightSwitch {
        serviceStatus(serviceId: $serviceId) {
            permissions {
                resource
                action
            }
            allowedActions
            serviceInstanceId
            overrideCatalogIds
            maintenanceUri
            banned
            launcherInfoDTO {
                catalogItemId
                appName
                namespace
            }
            message
            timeToShutdownInMs
            status
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