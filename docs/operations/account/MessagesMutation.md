# MessagesMutation

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation MessagesMutation($containerType: String!, $containerId: String!, $createMessageRequest: CreateMessageRequest!, $accountId: String!, $messageId: String!) {
    Messages {
        createMessage(containerType: $containerType, containerId: $containerId, createMessageRequest: $createMessageRequest) {
            tag
            type
            id
            uploadUrl
        }
        markMessageRead(accountId: $accountId, containerType: $containerType, containerId: $containerId, messageId: $messageId)
    }
}
```

## Variables
```json
{
    "containerType": "",
    "containerId": "",
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
    "accountId": "",
    "messageId": ""
}
```