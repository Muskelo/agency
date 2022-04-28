import "bootstrap";
import {createApp} from 'vue';

import { router } from './route';
// components
import App from './App.vue';

// create app
const app = createApp(App);
app.use(router);

app.mount('#app');
