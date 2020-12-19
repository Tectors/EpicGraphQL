# ActivityStreamQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query ActivityStreamQuery($id: String!) {
    ActivityStream {
        channel(id: $id) {
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
        myChannel {
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
        feed(id: $id) {
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
        myFeed {
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
        mySubscription {
            elements {
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
            paging {
                total
                count
                start
            }
        }
        myPersistentFeed {
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
    "id": ""
}
```