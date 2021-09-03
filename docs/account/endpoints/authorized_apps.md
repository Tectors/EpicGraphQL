# Account Authorized Apps
A request to get all the authorized applications authorized using the account settings page.

## Request
| URL | Method |
| - | - |
| https://www.epicgames.com/account/v2/authorized-apps | `GET` |

## Response
```json
{
   "socialData": {
      "githubDisplayName": "",
      "githubConnected": false,
      "psnDisplayName": "",
      "psnConnected": false,
      "xblDisplayName": "",
      "xblConnected": false,
      "twitchLinkUrl": "",
      "psnLinkUrl": "",
      "xboxLinkUrl": "",
      "nintendoLinkUrl": "",
      "githubLinkUrl": "",
      "steamLinkUrl": "",
      "authorizedAppClients": [
         {
            "clientId": "",
            "clientName": ""
         }
      ]
   },
   "externalAuths": [
      {
         "accountId": "",
         "type": "",
         "externalAuthId": "",
         "externalAuthIdType": "",
         "externalDisplayName": "",
         "authIds": [
            {
               "id": "",
               "type": ""
            }
         ],
         "dateAdded": "",
         "connected": false
      }
   ]
}
```