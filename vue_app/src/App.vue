<template>
  <Header />
  <router-view></router-view>
</template>

<script>
import Header from "./components/Header.vue";

export default {
  components: {
    Header,
  },
};
</script>

<style lang="scss">
$enable-cssgrid: true;
@import "../node_modules/bootstrap/scss/bootstrap.scss";
</style>


