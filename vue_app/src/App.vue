<template>
  <Header />
  <router-view></router-view>
</template>

<script>
import Header from "./components/Header.vue";
import { useCurrentUserStore } from "./stores/currentUser";

export default {
  data() {
    let currentUser = useCurrentUserStore();
    return {
      currentUser,
    };
  },
  components: {
    Header,
  },
  mounted() {
    this.currentUser.init();
  },
};
</script>

<style lang="scss">
$enable-cssgrid: true;
@import "../node_modules/bootstrap/scss/bootstrap.scss";
</style>


