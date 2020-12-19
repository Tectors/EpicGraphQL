# ActivityStreamMutation

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation ActivityStreamMutation($subscribeRequest: SubscribeRequest!, $postRequest: PostRequest!) {
    ActivityStream {
        subscribeMeToChannel(subscribeRequest: $subscribeRequest) {
            success
            message
        }
        postToChannel(postRequest: $postRequest) {
            id
            likes_number
            liked
            activity {
                ns
                created_at
                type
            }
            channels {
                id
                channelId
                name
                badge
                badgeColor
                lastRead
                unreadCount
                members {
                    accountId
                    displayName
                }
                subscribed
                subscriptions
                subscribers
                channel
                privacy
                type
            }
        }
    }
}
```

## Variables
```json
{
    "subscribeRequest": {
        "type": "USER, GROUP, COMMUNITY",
        "channelId": ""
    },
    "postRequest": {
        "type": "USER, GROUP, COMMUNITY",
        "channelId": "",
        "ns": "",
        "message": "",
        "link": "",
        "privacy": "PRIVATE, PUBLIC"
    }
}
```