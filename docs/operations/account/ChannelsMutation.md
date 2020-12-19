# ChannelsMutation

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation ChannelsMutation($createChannelRequest: CreateChannelRequest!, $containerId: String!, $editChannelRequest: EditChannelRequest!, $members: [String]!, $containerType: ContainerType!, $createMessageRequest: CreateMessageRequest!, $messageId: String!, $reaction: String!) {
    Channels {
        createChannel(createChannelRequest: $createChannelRequest) {
            channelId
            success
        }
        editChannel(containerId: $containerId, editChannelRequest: $editChannelRequest) {
            channelId
            success
        }
        leaveChannel(containerId: $containerId) {
            channelId
            success
        }
        deleteChannel(containerId: $containerId) {
            channelId
            success
        }
        addMembers(containerId: $containerId, members: $members) {
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
        createMessage(containerType: $containerType, containerId: $containerId, createMessageRequest: $createMessageRequest) {
            id
            entities {
                tag
                type
                id
                uploadUrl
            }
        }
        deleteMessage(containerType: $containerType, containerId: $containerId, messageId: $messageId) {
            success
        }
        reactToMessage(containerType: $containerType, containerId: $containerId, messageId: $messageId, reaction: $reaction) {
            success
        }
        deleteReactionToMessage(containerType: $containerType, containerId: $containerId, messageId: $messageId, reaction: $reaction) {
            success
        }
        readMessage(containerType: $containerType, containerId: $containerId, messageId: $messageId) {
            success
        }
    }
}
```

## Variables
```json
{
    "createChannelRequest": {
        "name": "",
        "badge": "ace, arm, bush, clown, crown, crab, dog, donut, finger, ghost, mushroom, ninja, pot, potato, radio, rainbow, seal, skele, unicorn",
        "badgeColor": [
            ""
        ],
        "members": [
            ""
        ]
    },
    "containerId": "",
    "editChannelRequest": {
        "name": "",
        "badge": "ace, arm, bush, clown, crown, crab, dog, donut, finger, ghost, mushroom, ninja, pot, potato, radio, rainbow, seal, skele, unicorn",
        "badgeColor": [
            ""
        ]
    },
    "members": "",
    "containerType": "channel, dm",
    "createMessageRequest": {
        "message": "",
        "entities": [
            {
                "tag": "",
                "title": "",
                "description": "",
                "type": "website, audio, video, image, gif, user, file, highlight",
                "contentType": "",
                "filename": "",
                "metadata": {
                    "key": "",
                    "value": ""
                }
            }
        ]
    },
    "messageId": "",
    "reaction": ""
}
```