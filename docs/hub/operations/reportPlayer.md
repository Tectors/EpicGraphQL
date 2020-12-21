# reportPlayer

Uhm, how did you find this?

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Query
```graphql
mutation reportPlayer($blockedUserRequested: Boolean!, $markedAsKnown: Boolean!, $details: String!, $reporterPlatform: String!, $offenderPlatform: String!, $partyId: String!, $reason: String!, $offenderAccountId: String!, $reporterAccountId: String!) {
  Fortnite {
    reportPlayer(report: undefined) {
     errorMessage
     errorCode
     status
     success
     __typename
    }
   __typename
  }
}
```

## Variables
```json
{
   "blockedUserRequested": "",
   "markedAsKnown": "",
   "details": "",
   "reporterPlatform": "",
   "offenderPlatform": "",
   "partyId": "",
   "reason": "",
   "offenderAccountId": "",
   "reporterAccountId": ""
}
```
| VARIABLES | DESCRIPTION | TYPE |
| - | - | - |
| blockedUserRequested | None | boolean |
| markedAsKnown | None | boolean |
| details | None | None |
| reporterPlatform | None | None |
| offenderPlatform | None | None |
| partyId | None | None |
| reason | None | None |
| offenderAccountId | None | None |
| reporterAccountId | None | None |

## Payload
```json
{
   "variables": {
      "reporterAccountId": "",
      "offenderAccountId": "",
      "reason": "",
      "partyId": "",
      "offenderPlatform": "",
      "reporterPlatform": "",
      "details": "",
      "markedAsKnown": "boolean",
      "blockedUserRequested": "boolean"
   },
   "query": "mutation reportPlayer($reporterAccountId: String!, $offenderAccountId: String!, $reason: String!, $partyId: String!, $offenderPlatform: String!, $reporterPlatform: String!, $details: String!, $markedAsKnown: Boolean!, $blockedUserRequested: Boolean!) { Fortnite { __typename reportPlayer(report: {reporterAccountId: $reporterAccountId, offenderAccountId: $offenderAccountId, reason: $reason, partyId: $partyId, offenderPlatform: $offenderPlatform, reporterPlatform: $reporterPlatform, details: $details, markedAsKnown: $markedAsKnown, blockedUserRequested: $blockedUserRequested, subGameName: \"Kairos\"}) { __typename success status errorCode errorMessage } } }"
}
```