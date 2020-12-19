import fetch from 'node-fetch';

export default class {
    constructor(token) {
        this.token = token;

        this.endpoint = 'https://graphql.epicgames.com/partyhub/graphql?sessionInvalidated=true';
    }

    async sendRequest(data) {
        return await (await fetch(this.endpoint, {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
                dnt: 1,
                Authorization: this.token
            }
        })).text();
    }
}