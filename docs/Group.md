# Group
This is not categorized due to the difference between tokens, and this is not public.

# Endpoint
Honestly never tried the partyhub one, but you could, it does work on the normal [/graphql](https://graphql.epicgames.com/graphql).

Works the same as the normal request with POST, though check Authorization for how to get the token for this endpoint.

## Queries

### Groups

```graphql
{
    Groups {
        groups(namespace: namespace) {
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

### Variables

Just replace the **\"namespace\"**, due to this request unable to have variables for some reason.

```json
{
    "namespace": ""
}
```

| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| namespace | The short/full name of the game. (eg. fortnite) | String |

### Payload
```json
{
   "query": "{ Groups { groups(namespace: \"namespace\") { mode name owner revision size namespace enabled description groupId members { isOwner account { name id displayName } joinedAt accountId } } } }"
}
```

### Create Group

```graphql
{
    Groups {
        groups(namespace: namespace) {
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

### Variables

Just replace the **\"namespace\"**, due to this request unable to have variables for some reason.

```json
{
    "namespace": ""
}
```

| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| namespace | The short/full name of the game. (eg. fortnite) | String |
| createGroupRequest | Information about the group your creating. | Object |

### createGroupRequest Variables
```json
{
    "name": "",
    "description": "",
    "motto": ""
}
```

| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| namespace | The short/full name of the game. (eg. fortnite) | String |
| description | Description about the group you're making. | String |
| name | Name of group. | String |
| motto | Reason of making the group???? (Unknown) | String |

### Payload
```json
{
   "query": "mutation { Groups { createGroup(namespace: \"namespace\", createGroupRequest: {name: \"name\", description: \"description\", motto: \"motto\"}) { name id createdAt } } }"
}
```

## Authorization
This is a very different way to get the Authorization token than normal, this is the only way I've found.

This is due because we are accessing information that one type of token has, so no other tokens will work.

This may be different due to the type of browser you are using.

## Step One
Go to [GraphQL](https://graphql.epicgames.com/) and login.

## Step Two
Press the button that is labled as "GraphQL".

## Step Three
Open your inspect element (may be different depending on your browser), go to Application and find the *Cookies* in Storage and click it, once clicked click on the url you went to.

Now you should see a bunch of cookies there, click the one called **EPIC_EG1**.

Image Here

Copy the token and your done getting your token.