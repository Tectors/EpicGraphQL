# Talon Service Initialize
Initialize a service (eg. checkout), possibly for security reasons.

## Request
| URL | Method |
| - | - |
| https://talon-service-prod.ak.epicgames.com/v1/init | `POST` |

## Payload
```json
{
    "flow_id": ""
}
```

## Parameters
- `flow_id`: the id of the action, eg. checkout_prod