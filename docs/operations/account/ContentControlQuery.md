# ContentControlQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query ContentControlQuery($name: String!, $pin: String!) {
    ContentControl {
        namespace(name: $name) {
            namespaceSetting {
                allowedToAcquire
                allowedToMakePurchases
                canSeeMatureLanguage
                canAcceptFriendRequest
                canRecieveInGameItems
                canSeeThirdPartyNames
                canDisplayMyUserName
                canSeeOtherPlayersNames
                canUseVoiceChat
                canVoiceChatWithUnknowns
            }
            userSetting {
                allowedToAcquire
                allowedToMakePurchases
                canSeeMatureLanguage
                canAcceptFriendRequest
                canRecieveInGameItems
                canSeeThirdPartyNames
                canDisplayMyUserName
                canSeeOtherPlayersNames
                canUseVoiceChat
                canVoiceChatWithUnknowns
            }
            result {
                allowedToAcquire
                allowedToMakePurchases
                canSeeMatureLanguage
                canAcceptFriendRequest
                canRecieveInGameItems
                canSeeThirdPartyNames
                canDisplayMyUserName
                canSeeOtherPlayersNames
                canUseVoiceChat
                canVoiceChatWithUnknowns
            }
        }
        verifyPin(pin: $pin) {
            pinCorrect
            err
        }
    }
}
```

## Variables
```json
{
    "name": "",
    "pin": ""
}
```