# Account Email Info
Returns information about the account's email (only shows censored email), if it can update the email as well as when will it able to update, and if it's verified as well as the last time it got verified.

## Request
| URL | Method |
| - | - |
| https://www.epicgames.com/account/v2/api/email/info | `GET` |

## Response
```json
{
   "isSuccess": true,
   "data": {
      "canUpdateEmail": true,
      "canUpdateNext": null,
      "default": {
         "email": "**@gmail.com",
         "verified": true,
         "default": true
      },
      "lastEmailUpdate": null,
      "unverified": null
   }
}
```