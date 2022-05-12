<template>
  <section class="container py-3">
    <!-- Pills content -->
    <div class="tab-content">
      <div class="tab-pane fade show active" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
        <form>
          <h4 class="text-center">Вход</h4>
          <!-- login input -->
          <div class="form-outline mb-4">
            <label class="form-label" for="login">Логин</label>
            <input v-model="login" type="text" id="login" class="form-control" />
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <label class="form-label" for="password">Пароль</label>
            <input v-model="password" type="password" id="password" class="form-control" />
          </div>

          <!-- Submit button -->
          <button @click="currentUser.login_f(login, password)" class="btn btn-primary mb-4 w-100">Войти</button>
          <p>{{currentUser.auth_header}}</p>
        </form>
      </div>
    </div>
    <!-- Pills content -->
  </section>
</template>

<script>
import { useCurrentUserStore } from "../stores/currentUser.js";
export default {
  data() {
    let currentUser = useCurrentUserStore();

    return {
      login: undefined,
      password: undefined,
      currentUser,
    };
  },
};
</script>

<style lang="scss" scoped>
.container {
  max-width: 600px;
}
</style>
