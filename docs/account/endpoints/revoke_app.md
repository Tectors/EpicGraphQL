# Account Revoke Apps
Revoke access to a application.

## Request
| URL | Method |
| - | - |
| https://www.epicgames.com/account/v2/authorized-apps/user-scopes/application/:id | `DELETE` |

## Parameters
- `id`: The application's id

## Response
```json
{
   "success": true,
   "data": {
      "applicationId": "",
      "consentStatus": "",
      "scopes": [
         ""
      ]
   }
}
```