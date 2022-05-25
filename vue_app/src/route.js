import {createRouter, createWebHashHistory} from "vue-router";

import Catalog from "./components/Catalog.vue";
import Item from "./components/Item.vue";
import CreateItem from "./components/CreateItem.vue";
import EditItem from "./components/EditItem.vue";
import Chat from "./components/Chat.vue";
import Login from "./components/Login.vue";
import Register from "./components/Register.vue";

const routes = [
    {
        path: '/',
        name: "home",
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
        path: '/item/edit/:id',
        name: 'edit_item',
        component: EditItem, props: true
    },
    {
        path: '/chat/',
        name: 'chat',
        component: Chat, props: true
    },
    {
        path: '/login/',
        name: 'login',
        component: Login, props: true
    },

    {
        path: '/register/',
        name: 'register',
        component: Register, props: true
    },

]
export const router = createRouter({
    history: createWebHashHistory(),
    routes,
})


