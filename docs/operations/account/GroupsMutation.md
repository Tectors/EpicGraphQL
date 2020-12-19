# GroupsMutation

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation GroupsMutation($namespace: String!, $createGroupRequest: CreateGroupRequest!, $groupId: String!, $accountId: String!) {
    Groups {
        createGroup(namespace: $namespace, createGroupRequest: $createGroupRequest) {
            id
            namespace
            name
            mode
            motto
            lang
            description
            owner
            size
            headcountLimit
            createdAt
            updatedAt
            enabled
            isOwner
            isAdmin
            revision
        }
        dismissGroup(groupId: $groupId) {
            success
        }
        leaveGroup(groupId: $groupId) {
            success
        }
        inviteUser(groupId: $groupId, accountId: $accountId) {
            accountId
            groupId
            groupHost
            sentAt
            message
            namespace
            name
        }
        acceptInvitation(groupId: $groupId) {
            accountId
            groupId
            groupHost
            sentAt
            message
            namespace
            name
        }
        declineInvitation(groupId: $groupId) {
            accountId
            groupId
            groupHost
            sentAt
            message
            namespace
            name
        }
    }
}
```

## Variables
```json
{
    "namespace": "",
    "createGroupRequest": {
        "name": "",
        "motto": "",
        "description": ""
    },
    "groupId": "",
    "accountId": ""
}
```