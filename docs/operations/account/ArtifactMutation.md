# ArtifactMutation

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation ArtifactMutation($addLabelRequest: AddLabelRequest!, $copyBinaryRequest: CopyBinaryRequest!) {
    Artifact {
        addLabel(addLabelRequest: $addLabelRequest) {
            success
        }
        copyBinary(copyBinaryRequest: $copyBinaryRequest) {
            success
        }
    }
}
```

## Variables
```json
{
    "addLabelRequest": {
        "organizationId": "",
        "productId": "",
        "label": "",
        "artifactId": "",
        "version": "",
        "platform": ""
    },
    "copyBinaryRequest": {
        "organizationId": "",
        "productId": "",
        "label": "",
        "sourceArtifactId": "",
        "targetArtifactId": "",
        "version": ""
    }
}
```