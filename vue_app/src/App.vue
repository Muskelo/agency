<script>
import Header from "./components/Header.vue";

export default {
  data() {
    return {
      message: "Hello World!",
      roles: "",
      login: "",
      password: "",
    };
  },
  methods: {
    getRoles() {
      this.fetchApi("/api/roles/", { roles: "roles" });
    },
    logout() {
      this.fetchApi("/api/roles/", { roles: "roles" }, true);
    },
  },
  mounted() {},
  components: {
    Header,
  },
};
</script>

<template>
  <Header />
  <p>{{ roles }}</p>
  <button @click="getRoles">Обновить роли</button>
  <button @click="logout">выйти роли</button>

  <label for="login">Логин</label>
  <input v-model="login" name="login" />

  <label for="password">Пароль</label>
  <input v-model="password" type="password" name="password" />

</template>

<style>
@import "../node_modules/bootstrap/dist/css/bootstrap.css";
</style>


