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
        },
        async updateCatalog(city, type,  rooms, min_price, max_price) {
            await items_list_api.get(`?city=${city}&type=${type}&rooms=${rooms}&min_price=${min_price}&max_price=${max_price}`)
                .then(response => this.items = response["data"])
        }

    }
})
