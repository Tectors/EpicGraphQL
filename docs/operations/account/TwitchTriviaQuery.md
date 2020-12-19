# TwitchTriviaQuery

[This is gotten from Terbau's gist, click to get to his gist!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query TwitchTriviaQuery($id: String!, $date: String!, $count: Int!, $triviaId: String!) {
    TwitchTrivia {
        currentTrivia {
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
        currentQuestion {
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
        getQuestion(id: $id) {
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
        list(date: $date, count: $count) {
            id
            createdDate
            eventName
            trivia {
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
        }
        trivia(triviaId: $triviaId) {
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
        currentTeams {
            teams {
                teamId
                name
                image
            }
            updatedBy
            updatedDate
            rvn
        }
        profile {
            id
            createdDate
            epicId
            epicDisplayName
            teamId
        }
        getAdmins
        getServerDate
        getHeartbeat
    }
}
```

## Variables
```json
{
    "id": "",
    "date": "",
    "count": 0,
    "triviaId": ""
}
```