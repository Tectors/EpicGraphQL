# TwitchTriviaMutation

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
mutation TwitchTriviaMutation($createTriviaRequest: CreateTriviaRequest!, $id: String!, $addQuestionRequest: AddQuestionRequest!, $removeQuestionRequest: RemoveQuestionRequest!, $triviaId: String!, $teamUpdateRequest: TeamUpdateRequest!, $submitAnswerRequest: SubmitAnswerRequest!, $teamId: Int!, $newUserId: String!, $userIdToRemove: String!, $heartbeatRequest: HeartbeatRequest!) {
    TwitchTrivia {
        createTrivia(createTriviaRequest: $createTriviaRequest) {
            id
            eventName
            createdDate
            createdBy
            secondsPerQuestion
            secondsBetweenQuestions
            questionIds
            questions {
                id
                question
                answers
                correctAnswerIndex
                createdDate
                createdBy
                startDate
                endDate
                nextStartDate
                scores(id: $id) {
                    teamId
                    name
                    correct
                    incorrect
                }
            }
        }
        addQuestion(addQuestionRequest: $addQuestionRequest) {
            id
            eventName
            createdDate
            createdBy
            secondsPerQuestion
            secondsBetweenQuestions
            questionIds
            questions {
                id
                question
                answers
                correctAnswerIndex
                createdDate
                createdBy
                startDate
                endDate
                nextStartDate
                scores(id: $id) {
                    teamId
                    name
                    correct
                    incorrect
                }
            }
        }
        removeQuestion(removeQuestionRequest: $removeQuestionRequest) {
            success
        }
        setCurrentTrivia(triviaId: $triviaId) {
            success
        }
        configureTeams(teamUpdateRequest: $teamUpdateRequest) {
            success
        }
        submitAnswer(submitAnswerRequest: $submitAnswerRequest) {
            success
        }
        setTeam(teamId: $teamId) {
            success
        }
        addAdmin(newUserId: $newUserId) {
            success
        }
        removeAdmin(userIdToRemove: $userIdToRemove) {
            success
        }
        stopTrivia {
            success
        }
        postHeartbeat {
            success
        }
        startHeartbeat(heartbeatRequest: $heartbeatRequest) {
            success
        }
    }
}
```

## Variables
```json
{
    "createTriviaRequest": {
        "secondsPerQuestion": 0,
        "secondsBetweenQuestions": 0,
        "eventName": ""
    },
    "id": "",
    "addQuestionRequest": {
        "triviaId": "",
        "question": "",
        "answers": [
            ""
        ],
        "correctAnswerIndex": 0
    },
    "removeQuestionRequest": {
        "triviaId": "",
        "questionId": ""
    },
    "triviaId": "",
    "teamUpdateRequest": {
        "teams": [
            {
                "name": "",
                "image": ""
            }
        ]
    },
    "submitAnswerRequest": {
        "userId": "",
        "teamId": 0,
        "questionId": "",
        "answerIndex": 0
    },
    "teamId": 0,
    "newUserId": "",
    "userIdToRemove": "",
    "heartbeatRequest": {
        "type": ""
    }
}
```