# OrganizationQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query OrganizationQuery {
    Organization {
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
    }
}
```

## Variables
```json
{}
```