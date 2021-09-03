# Talon Service Batch
Captcha and action logging for the api.

This is most likely being used for security due to it providing actions that are you are doing, such as checking out. 

## Request
| URL | Method |
| - | - |
| https://talon-service-prod.ak.epicgames.com/v1/phaser/batch | `POST` |

## Payload
```json
[
    {
        "errors": [],
        "event": "",
        "session": {
            "session": {
                "config": {
                    "h_captcha_config": {
                        "sdk_base_url": ""
                    }
                },
                "flow_id": "",
                "id": "",
                "ip_address": "",
                "plan": {
                    "h_captcha": {
                        "plan_name": "",
                        "site_key": ""
                    },
                    "mode": ""
                },
                "timestamp": "",
                "version": 0
            },
            "signature": ""
        },
        "timing": [
            {
                "event": "",
                "timestamp": ""
            }
        ]
    }
]
```

## Parameters