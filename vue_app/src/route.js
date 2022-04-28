import {createRouter, createWebHashHistory} from "vue-router";

import Catalog from "./components/Catalog.vue";
import Item from "./components/Item.vue";
import CreateItem from "./components/CreateItem.vue";
import Chat from "./components/Chat.vue";

const routes = [
    {
        path: '/',
        component: Catalog,
    },
    {
        path: '/item/:id',
        name: 'item',
        component: Item, props: true
    },
    {
        path: '/item/create',
        name: 'create_item',
        component: CreateItem, props: true
    },
    {
        path: '/chat/',
        name: 'chat',
        component: Chat, props: true
    },
 
]
export const router = createRouter({
    history: createWebHashHistory(),
    routes,
})


