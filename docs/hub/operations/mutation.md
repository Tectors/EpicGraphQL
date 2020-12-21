# mutation
These are mutation operations without a name.

# SocialBan
```graphql
mutation {
  SocialBan {
    acknowledgeMyBan {
     success
    }
  }
}
```

## Payload
```json
{
   "variables": {},
   "query": "mutation { SocialBan { ack: acknowledgeMyBan { success } } }"
}
```