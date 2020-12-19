# GroupsQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query GroupsQuery($id: String!, $groupId: String!, $accountId: String!, $countryCode: String!, $locale: String!, $newUserOnly: Boolean!, $externalAuthType: String!, $namespace: String!, $name: String!) {
    Groups {
        group(id: $id) {
            groupId
            namespace
            name
            motto
            lang
            description
            owner
            size
            headcountLimit
            createdAt
            updatedAt
            mode
            enabled
            isOwner
            isAdmin
            revision
            members(groupId: $groupId) {
                accountId
                admin
                isOwner
                joinedAt
                account(accountId: $accountId) {
                    id
                    displayName
                    email
                    isLoggedIn
                    unlinkedDieselPlatforms(countryCode: $countryCode, locale: $locale, newUserOnly: $newUserOnly)
                    externalAuths(externalAuthType: $externalAuthType) {
                        type
                        accountId
                        externalAuthId
                        externalDisplayName
                    }
                    isPublishDeveloper
                    isModerator
                    friendshipStatus
                    associatedOrganizations {
                        organizationId
                        name
                        country
                        created
                        financeCheckExempted
                        financeInfoFinished
                        ownerAccountId
                        slug
                        status
                        roles
                        isDeveloper
                    }
                    country
                    preferredLanguage
                    name
                    lastName
                    tfaEnabled
                }
            }
        }
        groupByName(namespace: $namespace, name: $name) {
            groupId
            namespace
            name
            motto
            lang
            description
            owner
            size
            headcountLimit
            createdAt
            updatedAt
            mode
            enabled
            isOwner
            isAdmin
            revision
            members(groupId: $groupId) {
                accountId
                admin
                isOwner
                joinedAt
                account(accountId: $accountId) {
                    id
                    displayName
                    email
                    isLoggedIn
                    unlinkedDieselPlatforms(countryCode: $countryCode, locale: $locale, newUserOnly: $newUserOnly)
                    externalAuths(externalAuthType: $externalAuthType) {
                        type
                        accountId
                        externalAuthId
                        externalDisplayName
                    }
                    isPublishDeveloper
                    isModerator
                    friendshipStatus
                    associatedOrganizations {
                        organizationId
                        name
                        country
                        created
                        financeCheckExempted
                        financeInfoFinished
                        ownerAccountId
                        slug
                        status
                        roles
                        isDeveloper
                    }
                    country
                    preferredLanguage
                    name
                    lastName
                    tfaEnabled
                }
            }
        }
        groups(namespace: $namespace) {
            groupId
            namespace
            name
            motto
            lang
            description
            owner
            size
            headcountLimit
            createdAt
            updatedAt
            mode
            enabled
            isOwner
            isAdmin
            revision
            members(groupId: $groupId) {
                accountId
                admin
                isOwner
                joinedAt
                account(accountId: $accountId) {
                    id
                    displayName
                    email
                    isLoggedIn
                    unlinkedDieselPlatforms(countryCode: $countryCode, locale: $locale, newUserOnly: $newUserOnly)
                    externalAuths(externalAuthType: $externalAuthType) {
                        type
                        accountId
                        externalAuthId
                        externalDisplayName
                    }
                    isPublishDeveloper
                    isModerator
                    friendshipStatus
                    associatedOrganizations {
                        organizationId
                        name
                        country
                        created
                        financeCheckExempted
                        financeInfoFinished
                        ownerAccountId
                        slug
                        status
                        roles
                        isDeveloper
                    }
                    country
                    preferredLanguage
                    name
                    lastName
                    tfaEnabled
                }
            }
        }
        members(groupId: $groupId) {
            accountId
            admin
            isOwner
            joinedAt
            account(accountId: $accountId) {
                id
                displayName
                email
                isLoggedIn
                unlinkedDieselPlatforms(countryCode: $countryCode, locale: $locale, newUserOnly: $newUserOnly)
                externalAuths(externalAuthType: $externalAuthType) {
                    type
                    accountId
                    externalAuthId
                    externalDisplayName
                }
                isPublishDeveloper
                isModerator
                friendshipStatus
                associatedOrganizations {
                    organizationId
                    name
                    country
                    created
                    financeCheckExempted
                    financeInfoFinished
                    ownerAccountId
                    slug
                    status
                    roles
                    isDeveloper
                }
                country
                preferredLanguage
                name
                lastName
                tfaEnabled
            }
        }
        myGroups(namespace: $namespace) {
            groupId
            namespace
            name
            motto
            lang
            description
            owner
            size
            headcountLimit
            createdAt
            updatedAt
            mode
            enabled
            isOwner
            isAdmin
            revision
            members(groupId: $groupId) {
                accountId
                admin
                isOwner
                joinedAt
                account(accountId: $accountId) {
                    id
                    displayName
                    email
                    isLoggedIn
                    unlinkedDieselPlatforms(countryCode: $countryCode, locale: $locale, newUserOnly: $newUserOnly)
                    externalAuths(externalAuthType: $externalAuthType) {
                        type
                        accountId
                        externalAuthId
                        externalDisplayName
                    }
                    isPublishDeveloper
                    isModerator
                    friendshipStatus
                    associatedOrganizations {
                        organizationId
                        name
                        country
                        created
                        financeCheckExempted
                        financeInfoFinished
                        ownerAccountId
                        slug
                        status
                        roles
                        isDeveloper
                    }
                    country
                    preferredLanguage
                    name
                    lastName
                    tfaEnabled
                }
            }
        }
        myGroupInvitations(namespace: $namespace) {
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
    "id": "",
    "groupId": "",
    "accountId": "",
    "countryCode": "",
    "locale": "",
    "newUserOnly": true,
    "externalAuthType": "",
    "namespace": "",
    "name": ""
}
```