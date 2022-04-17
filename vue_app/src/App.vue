<script>
import Header from "./components/Header.vue";
import ModalLogin from "./components/ModalLogin.vue";
import ModalRegister from "./components/ModalRegister.vue";
import { useCurrentUser } from "./stores/currentUser";

export default {
  data() {
    const currentUser = useCurrentUser();
    return {
      current_user_id: this.current_user.id,
      message: "Hello World!",
      roles: "",
      password: "",
      currentUser
    };
  },
  methods: {
    getRoles() {
      this.fetchApi("/api/roles/", {
        attributes: { roles: "roles" },
      });
    },
    login_() {
      this.current_user.setAuthorizationHeader(this.login, this.password);
    },
  },
  mounted() {},
  components: {
    Header,
    ModalLogin,
    ModalRegister,
  },
};
</script>

<template>
  <Header />
  <p>{{ currentUser.login }}</p>
  <button @click="getRoles">Обновить роли</button>

  <p>{{ login }}</p>

  <ModalLogin />
  <ModalRegister />
</template>

<style>
@import "../node_modules/bootstrap/dist/css/bootstrap.css";
</style>


