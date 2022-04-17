import {Buffer} from 'buffer';

export class CurrentUser {
    constructor() {
        this.authorizationHeader = "";
        this.data = {}
    }

    async login_f(login, password) {
        const authKey = Buffer.from(`${login}:${password}`).toString("base64");
        let authorizationHeader = `Basic ${authKey}`;

        const response = await fetch("/api/users/-1", {
            headers: {
                'Content-Type': 'application/json',
                "Authorization": authorizationHeader
            }
        })
        const data = await response.json();;
        for (const [key, value] of Object.entries(attributes)) {
            this.data[key] = data.user[value];
        }
        console.log(this.data)
        console.log(data)
        this.authorizationHeader = authorizationHeader;
    }

    logout() {
        this.data = {};
        this.authorizationHeader = "";
    }
}
