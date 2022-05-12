import {defineStore} from 'pinia'
import {defaults} from 'mande'
import {user_api} from "../api"

export const useCurrentUserStore = defineStore('currentUser', {
    state: () => {

        let local_auth_header = localStorage.getItem("auth_header");
        if (local_auth_header) {
            this.auth(local_auth_header);
        }
        return {
            id: 0,
            login: 0,
            number: 0,
            role: "",
        }
    },

    actions: {
        login_f(login, password) {
            auth_header = "Basic " + window.btoa(login + ":" + password);

            auth(auth_header)
            localStorage.setItem("auth_header", this.auth_header);
        },
        async auth(auth_header) {
            // set header to fetching data
            defaults.headers.Authorization = auth_header;
            user = await user_api.get(-1)["data"];
            if (user) {
                for (let key in user) {
                    this[key] = user[key]
                }
            } else {
                defaults.headers.Authorization = undefined;
            }
        },
        logout() {
            this.auth_header = undefined;
            localStorage.removeItem("auth_header");
        }
    },
})
