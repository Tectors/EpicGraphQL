# ChannelsQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query ChannelsQuery($containerId: String!, $containerType: ContainerType!, $sort: ChannelSort!, $messageId: String!) {
    Channels {
        channel(containerId: $containerId) {
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
        summary {
            channels {
                channelId
                name
                participants
                badge
                badgeColor
                lastRead
                unreadCount
                mostRecentMessage {
                    message {
                        id
                        containerType
                        containerId
                        accountId
                        message
                        timestamp
                        editedAt
                        reactions {
                            reaction
                            users
                        }
                        entities {
                            id
                            title
                            description
                            type
                            links {
                                contentType
                                url
                                profile
                                width
                                height
                                duration
                            }
                        }
                    }
                    users {
                        accountId
                        displayName
                    }
                }
                members
            }
            dms {
                channelId
                name
                participants
                badge
                badgeColor
                lastRead
                unreadCount
                mostRecentMessage {
                    message {
                        id
                        containerType
                        containerId
                        accountId
                        message
                        timestamp
                        editedAt
                        reactions {
                            reaction
                            users
                        }
                        entities {
                            id
                            title
                            description
                            type
                            links {
                                contentType
                                url
                                profile
                                width
                                height
                                duration
                            }
                        }
                    }
                    users {
                        accountId
                        displayName
                    }
                }
                members
            }
        }
        messages(containerType: $containerType, containerId: $containerId, sort: $sort) {
            messages {
                id
                containerType
                containerId
                accountId
                message
                timestamp
                editedAt
                reactions {
                    reaction
                    users
                }
                entities {
                    id
                    title
                    description
                    type
                    links {
                        contentType
                        url
                        profile
                        width
                        height
                        duration
                    }
                }
            }
            users {
                accountId
                displayName
            }
        }
        message(containerType: $containerType, containerId: $containerId, messageId: $messageId) {
            message {
                id
                containerType
                containerId
                accountId
                message
                timestamp
                editedAt
                reactions {
                    reaction
                    users
                }
                entities {
                    id
                    title
                    description
                    type
                    links {
                        contentType
                        url
                        profile
                        width
                        height
                        duration
                    }
                }
            }
            users {
                accountId
                displayName
            }
        }
    }
}
```

## Variables
```json
{
    "containerId": "",
    "containerType": "channel, dm",
    "sort": "asc, desc",
    "messageId": ""
}
```