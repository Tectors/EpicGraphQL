# Account Connections
A request to get all the connections linked to a account.

## Request
| URL | Method |
| - | - |
| https://www.epicgames.com/account/v2/connections/socialConnection/ajaxGet | `GET` |

## Query
- `lang`: language that it will output as, eg. en-US

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