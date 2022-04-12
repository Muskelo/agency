import { createApp } from 'vue'
import App from './App.vue'

import "bootstrap"

import fetchApi from "./_methods/fetch.js"

const app = createApp(App);

app.config.globalProperties.fetchApi = fetchApi;

app.mount('#app');
