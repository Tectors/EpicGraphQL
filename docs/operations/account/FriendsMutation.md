# FriendsMutation

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation FriendsMutation($friendToInvite: String!, $friendToDelete: String!, $suggestionToDismiss: String!, $friendToBlock: String!, $friendToUnblock: String!, $data: NotificationSettingsInput!, $friendId: String!, $alias: String!) {
    Friends {
        invite(friendToInvite: $friendToInvite) {
            success
        }
        deleteFriend(friendToDelete: $friendToDelete) {
            success
        }
        dismissFriendSuggestion(suggestionToDismiss: $suggestionToDismiss) {
            success
        }
        block(friendToBlock: $friendToBlock) {
            success
        }
        unblock(friendToUnblock: $friendToUnblock) {
            success
        }
        setNotificationSettings(data: $data) {
            offline {
                suppress_all
                send_invites
                send_pings
            }
            success
            message
            status
            online {
                suppress_all
                send_invites
                send_pings
            }
            suppress_all
        }
        setAlias(friendId: $friendId, alias: $alias) {
            success
        }
        deleteAlias(friendId: $friendId) {
            success
        }
    }
}
```

## Variables
```json
{
    "friendToInvite": "",
    "friendToDelete": "",
    "suggestionToDismiss": "",
    "friendToBlock": "",
    "friendToUnblock": "",
    "data": {
        "offline": {
            "suppress_all": true,
            "send_invites": true,
            "send_pings": true
        },
        "online": {
            "suppress_all": true,
            "send_invites": true,
            "send_pings": true
        },
        "suppress_all": true
    },
    "friendId": "",
    "alias": ""
}
```