<script>
import { useCurrentUser } from "./stores/currentUser";
/* components */
import Header from "./components/Header.vue";
import ModalLogin from "./components/ModalLogin.vue";
import ModalRegister from "./components/ModalRegister.vue";

export default {
  data() {
    const currentUser = useCurrentUser();

    return {
      currentUser,
    };
  },
  components: {
    Header,
    ModalLogin,
    ModalRegister,
  },
};
</script>

<template>
  <Header />

  <ModalLogin />
  <ModalRegister />
</template>

<style>
@import "../node_modules/bootstrap/dist/css/bootstrap.css";
</style>


