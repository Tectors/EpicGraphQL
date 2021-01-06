# Group
This is not categorized due to the difference between tokens, and this is not public.

# Endpoint
Honestly never tried the partyhub one, but you could, it does work on the normal [/graphql](https://graphql.epicgames.com/graphql), works the same as the normal request with POST, though check Authorization for how to get the token for this endpoint.

## Queries

### Groups

```graphql
{
    Groups {
        groups(namespace: \"fortnite\") {
            mode
            name
            owner
            revision
            size
            namespace
            enabled
            description
            groupId
            members {
                isOwner
                account {
                    name
                    id
                    displayName
                }
                joinedAt
                accountId
            }
        }
    }
}
```

### Payload
```json
{
   "query": "{ Groups { groups(namespace: \"fortnite\") { mode name owner revision size namespace enabled description groupId members { isOwner account { name id displayName } joinedAt accountId } } } }"
}
```

## Authorization
This is a very different way to get the Authorization token than normal, this is the only way I've found, it is because we are accessing information that one type of token has, so no other tokens will work.

This may differ depending on your browser.

## Step One
Go to [GraphQL](https://graphql.epicgames.com/) and login.

## Step Two
Press the button that is labled as "GraphQL".

## Step Three
Open your inspect element (may be different depending on your browser), go to Application and find the *Cookies* in Storage and click it, once clicked click on the url you went to, you should see a bunch of cookies there, click the one called **EPIC_EG1**.

![Application](https://github.com/Tectors/EpicGraphQL/raw/main/images/authforgroups.png)

Copy the token and your done getting your token.
