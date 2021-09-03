# Graphql

Epic Games's graphql requesting service, to do actions in applications and to request data and information.

You can access the graphql service using these routes:

- https://graphql.epicgames.com/graphql
- https://graphql.epicgames.com/partyhub/graphql
- https://graphql.unrealengine.com/ue/graphql

The endpoints above have been found using the Epic Games site and Unreal Engine documentation, you can view the endpoints being sent by the sites using your browers (if included) built in network tab.

## Authorization
Authorization may-be needed for the type of request, but due to graphql you are able to requst any query including account related ones, instead you'll be facing null and empty objects.

So if you had a endpoint such as a account or friend endpoint that requests for a friend, provide a graphql authorization in the header, I believe that the authorization can be anything client that is kairos or graphql related, don't quote me on that.

## Types
First, the normal GET request which is only bt query paramters:

- `operationName`: Operation's name
- `variables`: Variables (JSON) formatted into string format
- `extensions`: Extensions up-on the request

And lastly, which is the POST request that is a JSON request to the route, with the payload:

- `query`: Query that the user is trying to request
- `variables`: Variables that are used in the query
- `extensions`: Extensions up-on the request