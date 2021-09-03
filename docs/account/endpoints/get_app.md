# Account Get Apps
Get information such as authorized about a application.

## Request
| URL | Method |
| - | - |
| https://www.epicgames.com/account/v2/authorized-apps/user-scopes/application/:id | `GET` |

## Parameters
- `id`: The application's id

## Response
```json
{
   "success": true,
   "data": {
      "applicationId": "",
      "consentStatus": "",
      "scopes": []
   }
}
```