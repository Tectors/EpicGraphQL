# Account Verification Check
See if the account's email in question is verified.

## Request
| URL | Method |
| - | - |
| https://www.epicgames.com/account/v2/security/settings/ajaxCheckAccountVerification | `GET` |

## Response
```json
{
    "isSuccess": false,
    "isAccountVerified": false
}
```