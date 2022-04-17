import {defineStore} from 'pinia'
import {defaults} from 'mande'

import {usersApi} from "../api"

export const useCurrentUser = defineStore("currentUser", {
    state: () => {
        return {
            alerts: undefined,
        }
    },
    actions: {
        pushAlert(message, type) {
        }
    }

})
