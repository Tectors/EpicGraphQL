# MessagesQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query MessagesQuery($containerType: String!, $containerId: String!, $messageId: String!) {
    Messages {
        messages(containerType: $containerType, containerId: $containerId) {
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
    "containerType": "",
    "containerId": "",
    "messageId": ""
}
```