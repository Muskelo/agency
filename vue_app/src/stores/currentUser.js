import {defineStore} from 'pinia'
import {defaults} from 'mande'
import {user_api, users_list_api} from "../api"
import {useAlertsStore} from "./alerts"


export const useCurrentUserStore = defineStore('currentUser', {
    state: () => {
        return {
            id: undefined,
            login: undefined,
            number: undefined,
            role: "",
            auth_header: undefined
        };
    },
    actions: {
        async init() {
            if (localStorage.getItem("auth_header")) {
                this.auth(localStorage.getItem("auth_header"));
            }
        },
        async login_f(login, password) {
            let auth_header = "Basic " + window.btoa(login + ":" + password);
            const _ = await this.auth(auth_header);
            return this.id
        },
        logout() {
            localStorage.removeItem("auth_header");
            defaults.headers.Authorization = undefined;
            this.$reset();
        },
        async auth(auth_header) {
            // set header to fetching data
            defaults.headers.Authorization = auth_header;

            // try login
            await user_api.get(-1)
                .then(response => {
                    const user = response["data"];
                    console.log(user);

                    for (let key in user) {
                        this[key] = user[key];
                    }

                    // save
                    localStorage.setItem("auth_header", auth_header);
                    this.auth_header = auth_header;

                    return this.id;
                })
                .catch(error => {
                    defaults.headers.Authorization = undefined;

                    // make alert
                    const alerts = useAlertsStore();
                    alerts.addAlert("Вход", "Неверный логин или пароль", "error");

                    return false;
                });
        },
        async register(data) {
            await users_list_api.post({data: data});
        },
        hasRole(roles) {
            return Boolean(roles.indexOf(this.role) != -1)
        }

    },
})
