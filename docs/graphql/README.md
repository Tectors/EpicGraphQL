# GraphQL

<a href="https://gist.github.com/ToutinRoger/dd61991d4c1644454ff9aa4f0afe4713" target="_blank"><img align="right" width="302" height="172" src="https://raw.githubusercontent.com/ToutinRoger/FortniteFovChanger/main/port_later/usage-redirect.svg"></a>

Epic Games provides a graphql requesting service, to do actions in applications and to request data and information.

You can access the graphql service using these routes:

- [https://graphql.epicgames.com/graphql - *[Main Site]*](https://graphql.epicgames.com/graphql)
- [https://epicgames.com/graphql - *[Counter Part Of Main Site]*](https://epicgames.com/graphql)
- [https://graphql.epicgames.com/partyhub/graphql - *[Fortnite Party Hub]*](https://graphql.epicgames.com/partyhub/graphql)
- [https://graphql.unrealengine.com/ue/graphql - *[Unreal Engine Documentation]*](https://graphql.unrealengine.com/ue/graphql)

The endpoints above have been found using the Epic Games site and Unreal Engine documentation, you can view the endpoints being sent by the sites using your browers (if included) built in network tab.

## Authorization
Authorization may-be needed for the type of request, but due to graphql you are able to requst any query including account related ones, instead you'll be facing null and empty objects.

So if you had a endpoint such as a account or friend endpoint that requests for a friend, provide a graphql authorization in the header, I believe that the authorization can be anything client that is kairos or graphql related, don't quote me on that.

If a error code relating to permissions and not having them occurs, make sure you are using the correct authorization client. Find the client that has the permissions for your request at [MixV2/EpicResearch](https://github.com/MixV2/EpicResearch/blob/master/docs/auth/auth_clients.md).

## Types
First, the normal GET request which is only bt query paramters:

- `operationName`: Operation's name
- `variables`: Variables (JSON) formatted into string format
- `extensions`: Extensions up-on the request

And lastly, which is the POST request that is a JSON request to the route, with the payload:

- `query`: Query that the user is trying to request
- `variables`: Variables that are used in the query
- `extensions`: Extensions up-on the request

# History
There has been a history of Epic Games's GraphQL for example the main page for their services has changed, it use to be a [login page for GraphQL](https://graphql.epicgames.com/) but has since been removed, you can see the old page clicking [here!](https://web.archive.org/web/20200208114405/https://graphql.epicgames.com/)

It would use the [*graphqlWebsite*](https://github.com/MixV2/EpicResearch/blob/master/docs/auth/permissions/319e1527d0be4457a1067829fc0ad86e.md) to authorize and generate a token, then adding it to the cookie (I believe).

Once you authorized you would be able to request anything related to the services without authorization, if authorized with the cookie which is pretty cool.

## ReportPlayer Mutation
There is a mutation to report a player as much as you want for any reason at all, this was used for the **Fortnite Party Hub** application for mobile but can be used if you have a token.

It hasn't been used for malicious intents yet but still is very possible to cause some trouble in the community, you can report any user even a user not playing Fortnite!

## Groups
There is actually groups in the GraphQL service of Epic Games, people that have been researching their system and all have created groups and invited people to their groups, this probably was a scraped idea as it has been in the system for years without updates.

It was pretty suprising once I found people had created groups, and scared at the same time not knowning if I'll get banned or not, not sure but probably not, anyways it would of been cool to have groups in games.
