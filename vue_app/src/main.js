import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'

import "bootstrap"

import { fetchApi } from "./_methods/fetch.js"
import { CurrentUser } from "./_classes/current_user.js"

const app = createApp(App);

app.use(createPinia());

app.config.globalProperties.fetchApi = fetchApi;
app.config.globalProperties.current_user = new CurrentUser();

app.mount('#app');
