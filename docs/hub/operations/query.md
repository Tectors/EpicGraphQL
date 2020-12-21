# query
These are query operations without a name.

# Account & Fortnite Profile
```graphql
query {
  Fortnite {
    myProfile {
     id
    }
  }
  Account {
    myAccount {
      externalAuths {
       type
       externalDisplayName
      }
     country
     email
     displayName
     id
    }
  }
}
```
## Payload
```json
{
   "variables": {},
   "query": "query { Account { myAccount { id displayName email country externalAuths { externalDisplayName type } } }, Fortnite { myProfile { id } } }"
}
```

# Account & Fortnite Profile
```graphql
query {
  Fortnite {
    myProfile {
     id
    }
  }
  Account {
    myAccount {
      externalAuths {
       type
       externalDisplayName
      }
     country
     email
     displayName
     id
    }
  }
}
```
## Payload
```json
{
   "variables": {},
   "query": "query { Account { myAccount { id displayName email country externalAuths { externalDisplayName type } } }, Fortnite { myProfile { id } } }"
}
```

# Blocklist
```graphql
query {
  Friends {
    blockList(displayNames: true) {
     accountId
     displayName
    }
  }
}
```
## Payload
```json
{
   "variables": {},
   "query": "query { Friends { blockList(displayNames: true) { displayName, accountId } } }"
}
```

# SocialBan
```graphql
query {
  SocialBan {
    getMySocialBanSummary {
      bans {
       duration_s
       acked
       ends_at
       starts_at
      }
      warnings {
       acked
      }
    }
  }
}
```
## Payload
```json
{
   "variables": {},
   "query": "query { SocialBan { summary: getMySocialBanSummary { warnings { acked }, bans { starts_at, ends_at, acked, duration_s } } } }"
}
```