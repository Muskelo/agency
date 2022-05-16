import {defineStore} from 'pinia'
import {defaults} from 'mande'
import {user_api} from "../api"


export const useCurrentUserStore = defineStore('currentUser', {
    state: () => {
        return {
            id: undefined,
            login: undefined,
            number: undefined
        };
    },
    actions: {
        async init() {
            if (localStorage.getItem("auth_header")) {
                this.auth(localStorage.getItem("auth_header"));
            }
        },
        login_f(login, password) {
            let auth_header = "Basic " + window.btoa(login + ":" + password);
            this.auth(auth_header);
        },
        logout() {
            localStorage.removeItem("auth_header");
            defaults.headers.Authorization = undefined;
            this.$reset();
        },
        async auth(auth_header) {
            // set header to fetching data
            defaults.headers.Authorization = auth_header;

            const response = await user_api.get(-1);
            const user = response["data"];
            console.log(user);

            if (!user) {
                // if bad credationals
                defaults.headers.Authorization = undefined;
                return false;
            } else {
                for (let key in user) {
                    this[key] = user[key];
                }
            }

            localStorage.setItem("auth_header", auth_header);

            return user;
        }
    },
})
