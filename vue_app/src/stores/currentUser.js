import {defineStore} from 'pinia'
import {defaults} from 'mande'
import {user_api} from "../api"


export const useCurrentUserStore = defineStore('currentUser', {
    state: () => {
        return {
            data: {}
        };
    },
    getters: {
        getUser: async (state) => {
            if (!state.data) {
                return data
            }
            const local_auth_header = localStorage.getItem("auth_header");
        }
    },
    actions: {
        login_f(login, password) {
            let auth_header = "Basic " + window.btoa(login + ":" + password);

            this.auth(auth_header);
        },
        logout() {
            localStorage.removeItem("auth_header");
            defaults.headers.Authorization = undefined;
            this.data = undefined;
        },
        async auth(auth_header) {
            // set header to fetching data
            defaults.headers.Authorization = auth_header;

            const response = await user_api.get(-1);
            const user = response["data"];
            console.log(user);

            // if bad credationals
            if (!user) {
                defaults.headers.Authorization = undefined;
                return false;
            }

            // set data
            this.data = user;

            localStorage.setItem("auth_header", auth_header);

            return user;
        }
    },
})
