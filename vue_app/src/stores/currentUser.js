import {Buffer} from 'buffer';

import {defineStore} from 'pinia'
import {defaults} from 'mande'

import {usersApi} from "../api"

export const useCurrentUser = defineStore("currentUser", {
    state: () => {
        return {
            id: undefined,
            email: undefined,
            login: undefined,
            roles_id: undefined,
        }
    },
    actions: {
        async login_f(login, password) {
            const authKey = Buffer.from(`${login}:${password}`).toString("base64");
            defaults.headers.Authorization = `Basic ${authKey}`;

            await usersApi.get(-1)
                .then((data) => {
                    for (const [key, value] of Object.entries(data["user"])) {
                        this[key] = value;
                    }
                }).catch(() => {
                    alert("Неверный логин или пароль")
                    defaults.headers.Authorization = undefined;
                });
        },
        logout() {
            defaults.headers.Authorization = undefined;
            this.$reset()
        }
    }
})
