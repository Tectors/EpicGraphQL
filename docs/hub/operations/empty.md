# empty
These are empty operations without a name.

# Last Online Friends
```graphql
 {
  Presence {
    getLastOnlineSummary(circle: "friends", namespace: "fortnite") {
      summary {
       last_online
       circle
       namespace
       friendId
      }
    }
  }
}
```

## Payload
```json
{
   "variables": {},
   "query": "{ Presence { getLastOnlineSummary(namespace: "fortnite", circle: "friends") { summary { friendId namespace circle last_online } } } }"
}
```

# Broadcast enabled or not
```graphql
 {
  PresenceV2 {
    getSubscriptionSettings(namespace: "_") {
      broadcast {
       enabled
      }
    }
  }
}
```

## Payload
```json
{
   "variables": {},
   "query": "{ PresenceV2 { getSubscriptionSettings(namespace: "_") { broadcast { enabled } } } }"
}
```

# All subscriptions to Users
```graphql
 {
  PresenceV2 {
    getSubscriptions(namespace: "_") {
      summary {
       account_id
       subscribed_at
      }
    }
  }
}
```

## Payload
```json
{
   "variables": {},
   "query": "{ PresenceV2 { getSubscriptions(namespace: "_") { summary { subscribed_at account_id } } } }"
}
```

# Store Front
```graphql
 {
  Fortnite {
    getCurrentStoreOffers {
      storefronts {
        catalogEntries {
         assetName
          itemGrants {
           templateId
          }
        }
       name
      }
    }
  }
}
```

## Payload
```json
{
   "variables": {},
   "query": "{ Fortnite { getCurrentStoreOffers { storefronts { name catalogEntries { itemGrants { templateId } assetName } } } } }"
}
```

# Friend Notification Settings
```graphql
 {
  Friends {
    notificationSettings {
     message
     success
      offline {
       suppress_all
      }
    }
  }
}
```

## Payload
```json
{
   "variables": {},
   "query": "{ Friends { notificationSettings { offline { suppress_all } success message } } }"
}
```