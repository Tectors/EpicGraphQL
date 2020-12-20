# FriendsQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query FriendsQuery($limit: Int!, $countryCode: String!, $locale: String!, $newUserOnly: Boolean!, $externalAuthType: String!, $displayNames: Boolean!, $friendId: String!) {
    Friends {
        incomingInvites(limit: $limit) {
            accountId
            note
            displayName
            favorite
            connections {
                avatar
                id
                name
                type
            }
            account {
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
            alias
        }
        recentPlayers(displayNames: $displayNames) {
            accountId
            cohortId
            displayName
            namespace
            sessionId
            lastPlayed
        }
        summary(displayNames: $displayNames) {
            friends {
                accountId
                note
                displayName
                favorite
                connections {
                    avatar
                    id
                    name
                    type
                }
                account {
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
                alias
            }
            incoming {
                accountId
                note
                displayName
                favorite
                connections {
                    avatar
                    id
                    name
                    type
                }
                account {
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
                alias
            }
            outgoing {
                accountId
                note
                displayName
                favorite
                connections {
                    avatar
                    id
                    name
                    type
                }
                account {
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
                alias
            }
            suggested {
                accountId
                displayName
                connections {
                    avatar
                    id
                    name
                    type
                }
                friendsOnPlatforms
            }
            blocklist {
                accountId
                note
                displayName
                favorite
                connections {
                    avatar
                    id
                    name
                    type
                }
                account {
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
                alias
            }
        }
        suggested {
            accountId
            displayName
            connections {
                avatar
                id
                name
                type
            }
            friendsOnPlatforms
        }
        friends(displayNames: $displayNames) {
            accountId
            note
            displayName
            favorite
            connections {
                avatar
                id
                name
                type
            }
            account {
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
            alias
        }
        blockList(displayNames: $displayNames) {
            accountId
            note
            displayName
            favorite
            connections {
                avatar
                id
                name
                type
            }
            account {
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
            alias
        }
        friend(friendId: $friendId, displayNames: $displayNames) {
            accountId
            note
            displayName
            favorite
            connections {
                avatar
                id
                name
                type
            }
            account {
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
            alias
        }
        notificationSettings {
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
    }
}
```

## Variables
```json
{
    "limit": 0,
    "countryCode": "",
    "locale": "",
    "newUserOnly": true,
    "externalAuthType": "",
    "displayNames": true,
    "friendId": ""
}
```