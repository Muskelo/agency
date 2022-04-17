<script>
export default {
  data() {
    return {
      login: undefined,
      password: undefined,
      email: undefined,
    };
  },
  methods: {
    register() {
      let data = {
        user: {
          login: this.login,
          password: this.password,
          email: this.email,
        },
      };
      this.fetchApi("/api/users/", {
        data: data,
        method: "POST",
      });
    },
  },
};
</script>

<template>
  <div class="modal fade" id="modalRegister" tabindex="-1" aria-labelledby="modalRegisterLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalRegisterLabel">Регистрация</h5>
          <button class="btn-close" data-bs-dismiss="modal"></button>
        </div>

        <div class="modal-body">
          <div class="mb-3">
            <label for="login" class="form-label">Логин</label>
            <input v-model="login" type="text" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Почта</label>
            <input v-model="email" type="email" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Пароль</label>
            <input v-model="password" type="password" class="form-control" />
          </div>
        </div>

        <div class="modal-footer">
          <button class="btn btn-secondary" data-bs-dismiss="modal" type="button">
            Отмена
          </button>
          <button @click="register" type="button" data-bs-dismiss="modal" class="btn btn-primary">
            Войти
          </button>
        </div>
      </div>
    </div>
  </div>
</template>


<style>
</style>
