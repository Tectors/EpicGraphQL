# Account Status
Returns a bunch of information about the api throttling, and if it's ready to send requests to the api.

## Request
| URL | Method |
| - | - |
| https://www.epicgames.com/account/v2/retrieve-info/status | `GET` |

## Response
```json
{
   "state": "READY",
   "success": true,
   "status": 200,
   "isThrottled": false,
   "isAccountError": false
}
```