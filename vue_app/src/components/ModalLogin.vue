<template>
  <div class="modal fade" id="modalLogin" tabindex="-1" aria-labelledby="modalLoginLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalLoginLabel">Вход</h5>
          <button class="btn-close" data-bs-dismiss="modal"></button>
        </div>

        <div class="modal-body">
          <div class="mb-3">
            <label for="login" class="form-label">Логин</label>
            <input v-model="login" type="text" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Пароль</label>
            <input v-model="password" type="password" class="form-control" />
          </div>
        </div>

        <div class="modal-footer">
          <button class="btn btn-secondary" type="button" data-bs-dismiss="modal">
            Отмена
          </button>
          <button @click="login_f" type="button" class="btn btn-primary" data-bs-dismiss="modal">
            Войти
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {useCurrentUser} from "../stores/currentUser";

export default {
  data() {
    const currentUser = useCurrentUser();

    return {
      login: "",
      password: "",
      currentUser
    };
  },
  methods: {
    login_f() {
      this.currentUser.login_f(this.login, this.password);
    },
  },
};
</script>

<style>
</style>
