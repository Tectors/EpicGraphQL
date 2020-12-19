# AccountQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query AccountQuery($id: String!, $displayName: String!, $email: String!, $countryCode: String!, $locale: String!, $newUserOnly: Boolean!, $externalAuthType: String!, $accountIds: [String]!) {
    Account {
        account(id: $id, displayName: $displayName, email: $email) {
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
        myAccount {
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
        accounts(accountIds: $accountIds) {
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
```

## Variables
```json
{
    "id": "",
    "displayName": "",
    "email": "",
    "countryCode": "",
    "locale": "",
    "newUserOnly": true,
    "externalAuthType": "",
    "accountIds": ""
}
```