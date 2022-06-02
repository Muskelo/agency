import {defineStore} from 'pinia'
import {items_list_api} from "../api"

export const useCatalogStore = defineStore('catalog', {
    state: () => {
        return {
            items: Array(),
            city: "Казань",
            type: "",
            rooms: "",
            min_price: "",
            max_price: "",
            offset: 0,
            total: 0,
            pages: 0,
        }
    },
    actions: {
        async init() {
            await items_list_api.get()
                .then(response => this.items = response["data"]);
        },
        async updateCatalog() {
            await items_list_api.get(`?city=${this.city}&type=${this.type}&rooms
                =${this.rooms}&min_price=${this.min_price}&max_price=${this.max_price}&offset=${this.offset}`)
                .then(response => {
                    this.items = response["data"];
                    this.total = response["total"];
                    this.pages = Math.ceil(this.total / 20);
                })
        }

    }
})
