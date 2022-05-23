import {defineStore} from 'pinia'
import {items_list_api} from "../api"

export const useCatalogStore = defineStore('catalog', {
    state: () => {
        return {
            items: Array()
        }
    },
    actions: {
        async init() {
            await items_list_api.get()
                .then(response => this.items = response["data"]);
        }
    }
})
